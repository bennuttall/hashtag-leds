from time import sleep
from gpiozero import LED
from twython import TwythonStreamer

hashtags = {
    '#yes': LED(18),
    '#no': LED(15),
}

# Twitter application authentication
APP_KEY = 'erRilYZd8UzsXEFycmg'
APP_SECRET = 'Yt0fGlNvCyr1sFaC6ymdNhphHchaWbz0ECdotEXIQQ'
OAUTH_TOKEN = '1969690717-6a2RgVPXanSBaAjuie7EmUWZh78me8UZ6UxcM8V'
OAUTH_TOKEN_SECRET = 'UIrYV2XbYZC3vHzer6ZxIDwqVa0VvynQLDJYnSQV0R3xt'

# Setup callbacks from Twython Streamer
class BlinkyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print(data['text'].encode('utf-8'))
            self.led.on()
            sleep(0.5)
            self.led.off()

# Create streamer
for hashtag, led in hashtags.items():
    stream = BlinkyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    stream.statuses.filter(track=hashtag)
    stream.led = led
