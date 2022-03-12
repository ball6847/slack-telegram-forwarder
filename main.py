import os

from slack import RTMClient
import telegram

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
TELEGRAM_TARGET = os.environ['TELEGRAM_TARGET']
bot = telegram.bot.Bot(token=TELEGRAM_TOKEN)


@RTMClient.run_on(event='message')
def message(**payload):
    data = payload['data']
    channel_id = data['channel']
    message = data.get('text', [])
    print(
        f"Received message from slack channel#{channel_id}, forwarding to telegram#{TELEGRAM_TARGET}")
    try:
        bot.send_message(chat_id=TELEGRAM_TARGET, text=message)
    except telegram.error.BadRequest as e:
        print(f"Telegram bot error: {e.message}")


rtm_client = RTMClient(token=os.environ["SLACK_API_TOKEN"])
print("Bot is up and running")
rtm_client.start()
