from twython import TwythonStreamer

hashtags = {
    'yes': {
        "led": "hello",
        "count": 0,
    },
    'no': {
        "led": "goodbye",
        "count": 0,
    },
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
            for hashtag in hashtags:
                if hashtag in data['text']:
                    hashtags[hashtag]["count"] += 1
                    print(hashtag, hashtags[hashtag]["count"])

# Create streamer
stream = BlinkyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
terms = ','.join(hashtags)
stream.statuses.filter(track=terms)
