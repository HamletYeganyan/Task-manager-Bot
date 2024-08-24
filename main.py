import asyncio
import os
import pprint
from info import Ready_info_dict_Tasks, Ready_info_dict_Users
from src.database import async_session_factory
from src.models import UserORM, TaskORM
from src.ORM import select_column_items, select_one_item, update_table_object, insert_data_user, insert_data_task, insert_data_to_tables, Session_func
from sqlalchemy import select
import datetime

from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, or_f, StateFilter
from aiogram.utils.formatting import as_list, as_marked_section, Bold
from aiogram.types.message import ContentType
from aiogram import Bot, Dispatcher, types
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent
import hashlib

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import buttons

from bot_cmd_list import user_private_cmd
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher()

class Form(StatesGroup):
    description = State()
    task_status = State()
    task_deadline = State()

# --------------------------------------Commands---------------------------------------------------------------------------

@dp.message(CommandStart())
async def welcome(message: types.Message):
    user_id = message.from_user.id
    item = await select_one_item(UserORM, user_id)
    if item:
        first_name = item.first_name
        text = f"Well, hello, dear {first_name}. What would you like to do?"
        await message.answer(text)
    else:
        rid = Ready_info_dict_Users
        rid['user_id'] = user_id
        rid['first_name'] = message.from_user.first_name
        rid['last_name'] = message.from_user.last_name
        rid['username'] = message.from_user.username
        rid['created_at'] = datetime.datetime.now()
        await insert_data_to_tables("user", rid)

        text = f'Hello, dear {message.from_user.first_name}. You are already verified in TaskManagerBot. Write /add_task to add a task'

        await message.answer(text)

@dp.message(Command('add_task'))
async def add_task(message: types.Message, state: FSMContext):
    await state.set_state(Form.description)
    await message.answer('Write your task description.')

@dp.message(Command('tasks'))
async def add_task(message: types.Message):
    user_id = message.from_user.id

    async with async_session_factory() as session:
        stmt = select(TaskORM.description).where(TaskORM.user_id == str(user_id))
        result = await session.execute(stmt)
        
    descriptions = result.scalars().all()
    
    async with async_session_factory() as session:
        stmt = select(TaskORM.deadline).where(TaskORM.user_id == str(user_id))
        result = await session.execute(stmt)
    
    deadline = result.scalars().all()
        
    if descriptions:
        text = ''
        for i in range(len(deadline)):
           text += f'\n {descriptions[i]} | {deadline[i]}'
        # descriptions_text = "\n ".join(descriptions)
        await message.answer(f'Your tasks | deadline: {text}')
    else:
        await message.answer('You hav no tasks.')
        
# -----------------------------------------FSM schema--------------------------------------------------------------------

@dp.message(Form.description)
async def process_task(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await state.set_state(Form.task_status)  # Переключаемся на следующий шаг
    await message.answer("Now set your task's status.", reply_markup=buttons.create_task_status_buttons())

@dp.message(Form.task_deadline)
async def task_deadline(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    await state.update_data(task_deadline=message.text)
    data = await state.get_data()
    if data['task_deadline'] == 'None':
        await message.answer('Well done!')
        
    else:
        await message.answer(f'Deadline is {data["task_deadline"]}')
    
    # Сохраняем задачу в базе данных
    rid = Ready_info_dict_Tasks
    rid['user_id'] = str(user_id)
    rid['description'] = data['description']
    rid['task_id'] = hashlib.md5(str(data['description']).encode('utf-8')).hexdigest()
    rid['is_completed'] = data['task_status']
    rid['deadline'] = data['task_deadline']
    rid['created_at'] = str(datetime.datetime.now())
    rid['updated_at'] = str(datetime.datetime.now())
    await insert_data_to_tables('task', rid)
    
    await message.answer("Great! Your task is already in the database. You can use /tasks to view your tasks.")
    await state.clear()  # Завершаем FSM

# ------------------------------------------Callback query---------------------------------------------------------------

@dp.callback_query(lambda c: c.data in ['status_not_started', 'status_in_progress', 'status_completed'])
async def status_task(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(task_status=callback.data)
    
    if callback.data == 'status_in_progress':
        await state.set_state(Form.task_deadline)
        await callback.message.answer('You can add a deadline for your task write None to skip this step')
    else:
        user_id = callback.message.chat.id
        data = await state.get_data()
        rid = Ready_info_dict_Tasks
        rid['user_id'] = user_id
        rid['description'] = data['description']
        rid['task_id'] = hashlib.md5(str(data['description']).encode('utf-8')).hexdigest()
        rid['is_completed'] = callback.data[7:]
        await insert_data_to_tables('task', rid)
        await callback.message.answer("Great! Your task is already in the database. You can use /tasks to view your tasks.")
        await state.clear()

async def on_startup(bot):
    os.system('cls')
    print("🤖 - I'm starting to work ...")

async def main():
    try:
        dp.startup.register(on_startup)
        await bot.delete_webhook(drop_pending_updates=True)
        await bot.set_my_commands(commands=user_private_cmd, scope=types.BotCommandScopeAllPrivateChats())
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("🛑 - I'm finishing to work ...")
