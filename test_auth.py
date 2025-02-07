import tweepy
from config import TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET

# Authenticate with Twitter
auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

try:
    user = api.verify_credentials()
    print("Authentication successful!")
    print("Logged in as:", user.screen_name)
except Exception as e:
    print("Error during authentication:", e)
