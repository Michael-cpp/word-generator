# Word Generator Bot 📚

A Telegram bot that helps users learn vocabulary by providing random words with their English descriptions. The bot operates in two modes: interactive word generation and daily scheduled word delivery.

## Features

- 🎯 **Interactive Mode**: Generate words on-demand with a simple button click
- ⏰ **Daily Delivery**: Automatic daily word delivery to subscribed users
- 📖 **Rich Content**: Each word comes with the translation
- 👥 **User Management**: Automatic user registration and management
- 🐳 **Docker Support**: Easy deployment with Docker Compose

## Project Structure

```
word-generator/
├── data/
│   ├── words.csv          # Words with English descriptions
│   └── users.json         # Registered user chat IDs
├── daily_sender_bot.py    # Scheduled daily word delivery bot
├── interactive_bot.py     # Interactive word generation bot
├── utils.py              # Shared utility functions
├── docker-compose.yml    # Docker deployment configuration
└── README.md             # This file
```

## Components

### Interactive Bot (`interactive_bot.py`)
- Provides on-demand word generation via Telegram inline buttons
- Automatically registers new users
- Allows unlimited word requests until the dataset is exhausted

### Daily Sender Bot (`daily_sender_bot.py`)
- Sends one random word daily to all registered users
- Scheduled to run at 9 AM (configurable)
- Continues until all words are consumed

### Utilities (`utils.py`)
- `pop_random_word()`: Randomly generates a word
- `save_user()`: Registers new users
- `load_users()`: Retrieves list of registered users

## Setup & Installation

### Prerequisites
- Docker and Docker Compose
- Telegram Bot Token (obtain from [@BotFather](https://t.me/botfather))

### Environment Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd word-generator
   ```

2. **Create environment file:**
   ```bash
   echo "BOT_TOKEN=your_telegram_bot_token_here" > .env
   ```

3. **Run with Docker Compose:**
   ```bash
   docker-compose up -d
   ```

## Usage

### Starting the Bot
1. Find your bot on Telegram using the username you set with BotFather
2. Send `/start` command to begin
3. Click the "Generate" button to get your first word
4. You'll automatically receive daily words at 9 AM

### Example Word Format
```
📖 анализировать
To analyze
```

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

If you encounter any issues or have suggestions, please open an issue in the GitHub repository.

---

**Happy Learning! 🎓📚**
