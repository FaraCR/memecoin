import tweepy
import re
from config import TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET

# --- Authenticate with Twitter ---
auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# --- Define the list of Twitter accounts to track ---
# Replace these example handles with the actual Twitter handles you want to monitor.
tracked_users = ['crypto_oper', 'farmirmar']

# Convert screen names to user IDs (the streaming API requires numeric IDs)
user_ids = [str(api.get_user(screen_name=user).id) for user in tracked_users]

# --- Create a Stream Listener Class ---
class MemecoinStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        # Verify the tweet is from one of the tracked users
        if status.user.screen_name in tracked_users:
            tweet_text = status.text
            # Use regular expressions to check for keywords (memecoin, launch, coin)
            if re.search(r'\b(memecoin|launch|coin)\b', tweet_text, re.IGNORECASE):
                print(f"Alert: {status.user.screen_name} tweeted: {tweet_text}")

    def on_error(self, status_code):
        # Return False to disconnect the stream if rate limited (status code 420)
        if status_code == 420:
            return False

# --- Set Up and Start the Stream ---
listener = MemecoinStreamListener()
stream = tweepy.Stream(auth=api.auth, listener=listener)

print("Starting the Twitter stream...")

# Begin streaming tweets from the specified user IDs
stream.filter(follow=user_ids)
