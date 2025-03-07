import os
import requests
from dotenv import load_dotenv
import time
import json

load_dotenv()

# Twitter API v2 endpoint for liking a tweet (/2/users/:id/likes)
LIKE_TWEET_URL = "https://api.twitter.com/2/users/{user_id}/likes"

# Authenticate with Twitter API using OAuth 1.0a
def get_oauth_1_0a_headers():
    from requests_oauthlib import OAuth1

    # Gets API keys from environment variables
    consumer_key = os.getenv("TWITTER_API_KEY")
    consumer_secret = os.getenv("TWITTER_API_SECRET_KEY")
    access_token = os.getenv("TWITTER_ACCESS_TOKEN")
    access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

    # Create OAuth1 object
    oauth = OAuth1(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )
    return oauth

# Like a tweet using Twitter API v2
def like_tweet_v2(user_id, tweet_id):

    url = LIKE_TWEET_URL.format(user_id=user_id)
    headers = {"Content-Type": "application/json"}
    payload = {"tweet_id": tweet_id}

    try:
        # POST /2/users/:id/likes
        response = requests.post(
            url,
            auth=get_oauth_1_0a_headers(),
            headers=headers,
            data=json.dumps(payload),
        )

        # Raise an exception for HTTP errors
        response.raise_for_status()  
        print(f"Successfully liked tweet with ID: {tweet_id}")

    # Catch and handle exceptions     
    except requests.exceptions.HTTPError as e:
        if response.status_code == 429:
            # 429 = Rate Limit Exception handling
            reset_time = int(response.headers.get("x-rate-limit-reset", 0))
            current_time = time.time()
            # Compute time before retrying
            sleep_time = max(reset_time - current_time, 0) 
            print(f"Rate limit exceeded. Will try again in {sleep_time} seconds...")
            time.sleep(sleep_time)
            # Call function again after require idle time
            like_tweet_v2(user_id, tweet_id)
        else:
            # Catch and handle other HTTP errors
            print(f"Failed to like tweet: {e}")
            print(f"Response: {response.json()}")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():

    # Insert your User ID
    user_id = "INSTERT HERE"
     # Insert tweet ID to like. Currently on "https://x.com/ufc/status/1896577806559031757"
    tweet_id = "1896577806559031757"

    like_tweet_v2(user_id, tweet_id)

if __name__ == "__main__":
    main()