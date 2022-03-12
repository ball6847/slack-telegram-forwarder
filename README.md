# Slack Telegram Forwarder

A simple slack bot for forwarding message to telegram chat

## Running the bot using docker-compose

Clone the project, and prepare dependencies

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

edit docker-compose.yml (or create a new one) supply your information and save the file

```yml
version: '3'

services:
  slack-telegram-fwd:
    build: ./
    restart: unless-stopped
    environment:
      SLACK_API_TOKEN: slack-token
      TELEGRAM_TOKEN: telegram-token
      TELEGRAM_TARGET: telegram-chat-id

```

then, spin up the service using `docker-compose up -d`

## Acquiring Slack API Token

Follow this article to get one https://www.ibm.com/docs/en/z-chatops/1.1.1?topic=platform-creating-installing-slack-app
