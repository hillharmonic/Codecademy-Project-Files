import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

new_york_tweets = pd.read_json("new_york.json", lines=True)
london_tweets = pd.read_json("london.json", lines=True)
paris_tweets = pd.read_json("paris.json", lines=True)

print('# of NY Tweets: ', len(new_york_tweets))
print('# of London Tweets: ', len(london_tweets))
print('# of Paris Tweets: ', len(paris_tweets))

new_york_text = new_york_tweets["text"].tolist()
london_text = london_tweets["text"].tolist()
paris_text = paris_tweets["text"].tolist()

all_tweets = new_york_text + london_text + paris_text
labels = [0] * len(new_york_text) + [1] * len(london_text) + [2] * len(paris_text)

train_data, test_data, train_labels, test_labels = train_test_split(all_tweets, labels, test_size=0.2, random_state=1)
#print(len(train_data), len(test_data))

counter = CountVectorizer()
counter.fit(train_data)
train_counts = counter.transform(train_data)
test_counts = counter.transform(test_data)

classifier = MultinomialNB()
classifier.fit(train_counts, train_labels)
predictions = classifier.predict(test_counts)
print(predictions)

print(accuracy_score(test_labels, predictions))
print(confusion_matrix(test_labels, predictions))

# testing on a tweet of mine
tweet = "I swear I do work better when I'm listening to #musicals. My brain goes 'FIVE! SIX! SEVEN! EIGHT!'"
tweet_counts = counter.transform([tweet])
print(classifier.predict(tweet_counts))