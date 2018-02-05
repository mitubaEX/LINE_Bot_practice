import os
import sys
import json
from argparse import ArgumentParser
from configure import Configure
import requests

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)
conf = Configure()
line_bot_api = LineBotApi(conf.channel_access_token)
handler = WebhookHandler(conf.channel_secret)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
    talk_data = fetch_talk_data(event.message.text)
    line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=talk_data)
            )

def fetch_talk_data(message):
    payload = {'apikey': conf.talk_api_token, 'query': message}
    r = requests.post('https://api.a3rt.recruit-tech.co.jp/talk/v1/smalltalk', payload)
    return r.json()['results'][0]['reply']

if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', default=8000, help='port')
    arg_parser.add_argument('-d', '--debug', default=True, help='debug')
    options = arg_parser.parse_args()

    app.run(host="0.0.0.0", debug=options.debug, port=options.port)

