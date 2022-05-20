# Using the required libraries
from textblob import TextBlob as tb

print("Enter a text :")

# Taking input and converting it as a wordlist
text = tb(input())
list_ = text.words

# initializing positive and negative counters
pos = 0
neg = 0

# checking through the wordlist and for each condition increasing pos or neg counter by one respectively
# else if pos==0,neg==0 print input as neutral

for word in list_:

    if tb(word).sentiment.polarity > 0:

        pos += 1

    elif tb(word).sentiment.polarity < 0:

        neg += 1

if pos > 0:

    print("Positive words are:", pos)

else:

    print("No positive words are found")

if neg > 0:

    print("negative words :", neg)

else:

    print("No negative words are found")

if pos == 0 and neg == 0:

    print("Your input's sentiment is neutral")
