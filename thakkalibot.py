import tweepy
from os import getenv
from dotenv import load_dotenv
import time

load_dotenv()

api_key = getenv("API_KEY")
api_key_secret = getenv("API_KEY_SECRET")
access_token = getenv("ACCESS_TOKEN")
access_token_secret = getenv("ACCESS_TOKEN_SECRET")


def api():
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    return tweepy.API(auth)

def tweet(api, message, image_path):
    api.update_status_with_media(message, image_path)

api = api()
while(True):
    tweet(api, "Thakkali", r"tomoto.jpg")
    time.sleep(86400)
    print("bot posted a pic")
