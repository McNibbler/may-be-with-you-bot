#################################################################
# May be with you twitter bot									#
# By Thomas Kaunzinger											#
# May 3, 2019													#
#																#
# Dumb Twitter bot to post "[Month] the [date]th be with you."	#
# given the current date.										#
#																#
# To use this bot, include a text file in the root directory	#
# with four lines of the following keys in order...				#
#																#
# public api key 												#
# private api key 												#
# public access token 											#
# private access token 											#
#################################################################

# Include libraries
import tweepy
from datetime import datetime

# Reads from the private apikeys text file
with open('apikeys.txt', 'r') as file:
	data = file.readlines()

# Readlines() likes to add the newline character for some reason
for i in range(len(data)):
	data[i] = data[i].replace('\n', '')

# Creates an API with the imported credentials
pub_key = data[0]
secret_key = data[1]
pub_token = data[2]
secret_token = data[3]

auth = tweepy.OAuthHandler(pub_key, secret_key)
auth.set_access_token(pub_token, secret_token)
api = tweepy.API(auth)

# Generates the string to tweet
def get_tweet():
    month = datetime.now().strftime('%B')
    day = str(datetime.now().day) 
    tweet = month + " the " + day + "th be with you."
    return tweet

# Sends the tweet
def send_tweet():
    tweet = get_tweet()
    status = api.update_status(tweet)
    print(status.id)

# Execute me uwu
if __name__ == '__main__':
	send_tweet()


# P.S. Python is a dumb language
