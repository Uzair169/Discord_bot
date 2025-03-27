# Ollama Discord Bot

Ollama Discord Bot is a simple Discord bot that interacts with users using OpenAI's Ollama chat models. It can respond to messages, answer questions, and summarize recent chat messages.

## Features
- Responds to a simple `/hello` command.
- Answers user questions with the `/ask` command using the Ollama AI model.
- Summarizes the last 10 messages in a channel using the `/summarise` command.

## Requirements
- Python3
- A Discord bot token
- OpenAI's Ollama library
- llama model of your choice

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/ollama-discord-bot.git
   cd ollama-discord-bot
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```sh
   pip install ollama dotenv
   ollama run llama3.2:1b
   ```

4. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add your Discord bot token:
     ```
     Discord_bot_token=your_discord_bot_token_here
     ```

## Usage

1. Run the bot:
   ```sh
   python bot.py
   ```

2. Invite the bot to your Discord server and use the following commands:
   - `/hello` - Greets the user.
   - `/ask <question>` - Asks Ollama AI a question.
   - `/summarise` - Summarizes the last 10 messages in the channel.

## Notes
- Ensure your bot has the correct permissions to read and send messages.
- Modify the `ollama.chat()` function to change AI behavior.

## Contributing
Feel free to submit pull requests or report issues.

