import requests

f = open('token.txt', 'r')
bot_token = f.read()
f.close()


class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json


audio_bot = BotHandler(bot_token)


def main():
    new_offset = None

    while True:
        updates = audio_bot.get_updates(new_offset)
        print(updates)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
