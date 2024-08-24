from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton

def create_task_status_buttons():
    buttons = [
        InlineKeyboardButton(text="Not Started", callback_data="status_not_started"),
        InlineKeyboardButton(text="In Progress", callback_data="status_in_progress"),
        InlineKeyboardButton(text="Completed", callback_data="status_completed"),
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=[buttons])
    return keyboard


def main_menu_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton('/add_task'))
    keyboard.add(KeyboardButton('/tasks'))
    keyboard.add(KeyboardButton('/help'))
    return keyboard



