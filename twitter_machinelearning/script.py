import pandas as pd
import numpy as np
from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

all_tweets = pd.read_json("random_tweets.json", lines=True)

print(all_tweets.columns)
print(all_tweets.loc[0]['text'])

#print(all_tweets.loc[0]['user']['location'])

#print(all_tweets['retweet_count'])
median_retweets = all_tweets['retweet_count'].median()
all_tweets['is_viral'] = np.where(all_tweets['retweet_count'] > median_retweets , 1, 0)

#print(all_tweets.is_viral.value_counts())

all_tweets['tweet_length'] = all_tweets.apply(lambda tweet: len(tweet['text']), axis=1)
all_tweets['followers_count'] = all_tweets.apply(lambda tweet: tweet['user']['followers_count'], axis=1)
all_tweets['friends_count'] = all_tweets.apply(lambda tweet: tweet['user']['friends_count'], axis=1)
all_tweets['hashtag_count'] = all_tweets.apply(lambda tweet: tweet['text'].count("#"), axis=1)

#print(all_tweets['hashtag_count'])

labels = all_tweets['is_viral']
data = all_tweets[['tweet_length', 'followers_count', 'friends_count', 'hashtag_count']]
scaled_data = scale(data, axis=0)

#print(scaled_data[0:5])

train_data, test_data, train_labels, test_labels = train_test_split(scaled_data, labels, test_size=0.2, train_size=0.8, random_state=1)

scores = []
for k in range(1,200):
    classifier = KNeighborsClassifier(n_neighbors=k)
    classifier.fit(train_data, train_labels)
    score = classifier.score(test_data, test_labels)
    scores.append(score)

plt.plot(range(1,200), scores)
#plt.show()
# best was a k around 43 with a .62 probability

