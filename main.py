import twython
from twython import Twython
CONSUMER_KEY = ""    # add here your key
CONSUMER_SECRET = "" # add here your consumer_secret

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET)

# search for tweets containing the phrase "data science" 
# add other search keywords you want to test
for status in twitter.search(q='"data science"')["statuses"]:
    user = status["user"]["screen_name"].encode('utf-8')
    text = status["text"].encode('utf-8')
    print(user, ":", text)
    print()
