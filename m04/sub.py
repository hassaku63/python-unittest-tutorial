import os
from slack import WebClient
client = None


def _get_client():
    global client
    if client is None:
        client = WebClient(token=os.environ.get('SLACK_API_TOKEN'))
    return client


def notify(text):
    slk = _get_client()
    slk.chat_postMessage(
        channel=os.environ.get('SLACK_CHANNEL'),
        text=text
    )