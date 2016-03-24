from time import sleep
from gpiozero import PWMLED
from twython import TwythonStreamer
from signal import pause

hashtags = {
    '#yes': PWMLED(18),
    '#no': PWMLED(15),
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
            if self.count < 1:
                self.count += 0.01
            self.led.value = self.count
            

# Create streamer
for hashtag, led in hashtags.items():
    stream = BlinkyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    stream.statuses.filter(track=hashtag)
    stream.led = led
    stream.led.off()
    stream.count = 0

pause()
