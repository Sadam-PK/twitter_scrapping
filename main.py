import pandas as pd
import snscrape.modules.twitter as sntwitter

query = '(from:elonmusk) until:2020-01-01 since:2010-01-01'
tweets = []
limits = 100

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    # print(vars(tweet))
    # break
    if len(tweets) == limits:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
print(df)
