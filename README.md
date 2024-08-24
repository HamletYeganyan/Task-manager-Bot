# Task Manager Bot

This is a Telegram bot built with [Aiogram 3.x](https://docs.aiogram.dev/en/latest/) for managing tasks. The bot allows users to track their tasks by selecting different statuses and storing user data in a PostgreSQL database.

## Features

- **User Registration**: Automatically registers users in the database when they start the bot.
- **Task Status Management**: Users can select the status of their tasks using inline buttons.
- **Persistent Storage**: User and task data are stored in a PostgreSQL database using SQLAlchemy ORM.
- **Asynchronous Operation**: Fully asynchronous operation using `aiogram` and `asyncpg`.

## Requirements

- Python 3.8+
- PostgreSQL
- Required Python packages (see [Installation](#installation))

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/Task-manager-Bot.git
    cd Task-manager-Bot
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    ./venv/Scripts/activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure environment variables**:
    - Create a `.env` file in the root directory and add your Telegram bot token and database credentials:
    ```
    API_TOKEN=your_telegram_bot_token_here
    DATABASE_URL=postgresql+asyncpg://username:password@localhost/dbname
    ```

5. **Run database migrations** (if applicable):
    - If you have database migrations set up, run them to create the necessary tables.

6. **Run the bot**:
    ```bash
    python main.py
    ```

## Usage

- Start the bot by sending `/start`. The bot will greet you and register your information in the database.
- If you restart the bot, it will recognize you and offer options to manage your tasks.
- Use the inline buttons to select the status of your tasks.

## Project Structure

- `main.py`: The main entry point of the bot.
- `buttons.py`: Contains the button constructor for task status selection.
- `src/`: Contains models and database-related code.
- `.env`: Stores environment variables (not included in the repository).

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Create a new Pull Request
