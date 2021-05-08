import nltk
nltk.downloader.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
SIA = SentimentIntensityAnalyzer()
def fetch_sentiment(sentence):
    sentiment = SIA.polarity_scores(sentence)
    #print(sentiment)
    if(sentiment["neg"]>0.5):
        return "neg"
    else:
        return "pass"
        
    

print(fetch_sentiment("I am very sad and not happy"))
