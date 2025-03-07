Setup Instructions

1. Install Dependencies

    Ensure you have Python installed (version 3.7 or later). Install the required libraries using:

    pip install requests python-dotenv requests-oauthlib

2. Set Up API Credentials

    Modify the .env file in the same directory as the script and replace fake credentials with your Twitter API credentials:

3. Customize the Script

    Edit the main() function in like.py to specify the user_id and tweet_id you want to like.

    user_id = "your_twitter_user_id"
    tweet_id = "tweet_id_to_like"

    Replace these values with your actual Twitter user ID and the tweet ID you want to like.

4. Run the Script

    Execute the script using:

    python like.py


Notes:

    - This script includes basic error handling for rate limits and HTTP errors.

    - Ensure your Twitter Developer account has the correct permissions to like tweets using the API. (Read and Write)

