import os

from slack import RTMClient
import telegram

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
TELEGRAM_TARGET = os.environ['TELEGRAM_TARGET']
bot = telegram.bot.Bot(token=TELEGRAM_TOKEN)


def render_message(data):
    message = data.get('text', [])
    if message != '':
        return message
    lines = []
    attachments = data.get('attachments', [])
    if len(attachments) > 0:
        if data['bot_profile']['name']:
            lines.append(f"*{data['bot_profile']['name']}*")
        lines.extend([
            f"{attachments[0]['title']}",
            "",
            attachments[0]['text']
        ])
    return "\n".join(lines)


@RTMClient.run_on(event='message')
def message(**payload):
    data = payload['data']
    channel_id = data['channel']
    message = render_message(data)

    print(
        f"Received message from slack channel#{channel_id}, forwarding to telegram#{TELEGRAM_TARGET}")
    try:
        bot.send_message(TELEGRAM_TARGET, message, parse_mode="markdown")
    except telegram.error.BadRequest as e:
        print(f"Telegram bot error: {e.message}")


rtm_client = RTMClient(token=os.environ["SLACK_API_TOKEN"])
print("Bot is up and running")
rtm_client.start()
