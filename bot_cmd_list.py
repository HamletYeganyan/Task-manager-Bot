from aiogram.types import BotCommand
user_private_cmd = [
    BotCommand(command='start', description='Запуск бота'),
    BotCommand(command='add_task', description='Добавить новую задачу'),
    BotCommand(command='tasks', description='Список моих задач'),
    BotCommand(command='edit_task', description='Редактировать задачу'),
    BotCommand(command='delete_task', description='Удалить задачу'),
    BotCommand(command='profile', description='Мой профиль'),
    BotCommand(command='edit_profile', description='Редактировать профиль'),
    BotCommand(command='help', description='Помощь'),
    BotCommand(command='about', description='О боте'),
]
