Ready_info_dict_Users = {
    'user_id': None,                     # Идентификатор пользователя (id из таблицы `users`)                 # Telegram ID пользователя
    'username': None,                    # Имя пользователя (username в Telegram)
    'first_name': None,                  # Имя пользователя
    'last_name': None,                   # Фамилия пользователя
    'created_at': None,                  # Время регистрации пользователя
    'updated_at': None,                  # Время последнего обновления данных пользователя
    'task_count': '0',                     # Количество задач, созданных пользователем
    'completed_task_count': '0',           # Количество выполненных задач пользователя
    'incomplete_task_count': '0',          # Количество невыполненных задач пользователя
    'last_task_created': None,           # Время создания последней задачи
    'last_task_updated': None,  # Время последнего обновления задачи
}

Ready_info_dict_Tasks = {
    'user_id': None,
    'task_id': None,                    # Идентификатор пользователя (ссылка на таблицу `users`)
    'description': None,                # Описание задачи
    'deadline': None,                   # Дедлайн выполнения задачи
    'is_completed': False,              # Статус выполнения задачи (True или False)
    'created_at': None,                 # Время создания задачи
    'updated_at': None,                 # Время последнего обновления задачи
}
