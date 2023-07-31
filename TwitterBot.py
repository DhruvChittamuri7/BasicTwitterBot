import requests
from requests_oauthlib import OAuth1
import os
import json
from Secret import consumer_key, consumer_secret, access_token, access_token_secret, bearer_token


    # format in the correct manner for the twitter post request
def format_text(fact):
   return {"text": "{}".format(fact)}

# connect text to the oath
def connect_to_oauth(consumer_key, consumer_secret, acccess_token, access_token_secret):
   url = "https://api.twitter.com/2/tweets"
   auth = OAuth1(consumer_key, consumer_secret, acccess_token, access_token_secret)
   return url, auth

# post the actual tweet
def send_tweet(auth, url, payload, reply_id):
    # reply_id - an optional parameter for the tweet that is to be replied to
    if reply_id:
        payload["reply"] = {"in_reply_to_tweet_id": f"{reply_id}"}
    request = requests.post(
        auth=auth, url=url, json=payload, headers={"Content-Type": "application/json"}
    )


# user prompting
text = input("What should I tweet out?\n")

# content that is to be tweeted (predefined)
#stext = "XXXXX"

# formatting the text in the correct way
payload = format_text(text)

# connecting to auth with the appropriate keys
# using OAuth1 User Context
url, auth = connect_to_oauth(
     consumer_key, consumer_secret, access_token, access_token_secret
)

# publish the actual tweet, reply_id an optional field
send_tweet(auth=auth, url=url, payload=payload, reply_id=XXXXX)

