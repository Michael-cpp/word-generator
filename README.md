# Word Generator Bot 📚

A Telegram bot that helps users learn vocabulary by providing random words with their English descriptions. The bot operates in two modes: interactive word generation and daily scheduled word delivery.

## Features

- 🎯 **Interactive Mode**: Generate words on-demand with a simple button click
- ⏰ **Daily Delivery**: Automatic daily word delivery to subscribed users
- 📖 **Rich Content**: Each word comes with detailed English descriptions
- 🔄 **No Duplicates**: Words are consumed from the dataset to avoid repetition
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
- `pop_random_word()`: Randomly selects and removes a word from the CSV
- `save_user()`: Registers new users
- `load_users()`: Retrieves list of registered users

### Word Dataset (`data/words.csv`)
- Contains words with English translations and descriptions
- Covers various categories: verbs, adjectives, nouns, and concepts
- Words are removed after being selected to prevent repetition

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

### Manual Installation

1. **Install dependencies:**
   ```bash
   pip install python-telegram-bot==20.6 apscheduler
   ```

2. **Set environment variable:**
   ```bash
   export BOT_TOKEN="your_telegram_bot_token_here"
   ```

3. **Run the bots:**
   ```bash
   # For interactive mode
   python interactive_bot.py
   
   # For daily delivery (in separate terminal)
   python daily_sender_bot.py
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
To analyze - to examine in detail in order to understand or interpret.
```

## Configuration

### Changing Daily Delivery Time
Edit the `hour` parameter in `daily_sender_bot.py`:
```python
scheduler.add_job(send_daily_word, 'cron', hour=9)  # Change 9 to your preferred hour
```

### Adding More Words
Add new entries to `data/words.csv` following the format:
```csv
word,description
новое_слово,New word - description in English.
```

## Docker Services

The `docker-compose.yml` defines two services:

- **word_bot_interactive**: Handles user interactions and on-demand word generation
- **word_bot_daily**: Manages scheduled daily word delivery

Both services:
- Use Python 3.11 slim image
- Auto-restart unless manually stopped
- Share the same data volume for consistency
- Install required dependencies on startup

## File Descriptions

| File | Purpose |
|------|---------|
| `interactive_bot.py` | Telegram bot for interactive word generation |
| `daily_sender_bot.py` | Scheduled bot for daily word delivery |
| `utils.py` | Shared functions for word and user management |
| `data/words.csv` | Database of words and descriptions |
| `data/users.json` | List of registered user chat IDs |
| `docker-compose.yml` | Container orchestration configuration |

## Data Management

- **Words**: Stored in CSV format, consumed randomly without replacement
- **Users**: Automatically saved to JSON file when they interact with the bot
- **Persistence**: Data directory is mounted as Docker volume to persist across container restarts

## Error Handling

- Failed message deliveries are logged but don't stop the service
- Missing data files are handled gracefully
- Invalid JSON in user file is recovered automatically

## Contributing

1. Fork the repository
2. Add new words to `data/words.csv`
3. Test with both bot modes
4. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

If you encounter any issues or have suggestions, please open an issue in the GitHub repository.

---

**Happy Learning! 🎓📚**
