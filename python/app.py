import time
import RPi.GPIO as GPIO
from twython import TwythonStreamer

# Search terms
TERMS = '#yes'

# GPIO pin number of LED
LED = 22

# Twitter application authentication
APP_KEY = 'erRilYZd8UzsXEFycmg'
APP_SECRET = 'Yt0fGlNvCyr1sFaC6ymdNhphHchaWbz0ECdotEXIQQ'
OAUTH_TOKEN = '1969690717-6a2RgVPXanSBaAjuie7EmUWZh78me8UZ6UxcM8V'
OAUTH_TOKEN_SECRET = 'UIrYV2XbYZC3vHzer6ZxIDwqVa0VvynQLDJYnSQV0R3xt'

# Setup callbacks from Twython Streamer
class BlinkyStreamer(TwythonStreamer):
        def on_success(self, data):
                if 'text' in data:
                        print data['text'].encode('utf-8')
                        print
                        GPIO.output(LED, GPIO.HIGH)
                        time.sleep(0.5)
                        GPIO.output(LED, GPIO.LOW)

# Setup GPIO as output
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

# Create streamer
try:
        stream = BlinkyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        stream.statuses.filter(track=TERMS)
except KeyboardInterrupt:
        GPIO.cleanup()

