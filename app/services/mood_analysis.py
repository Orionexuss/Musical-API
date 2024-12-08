import spacy
from textblob import TextBlob

nlp = spacy.load("en_core_web_sm")

def analyze_sentiment(text: str) -> str:

    doc = nlp(text)
    clean_text = " ".join([token.lemma_ for token in doc if not token.is_stop])

    # Here we will calculate the mood with TextBlob
    analysis = TextBlob(clean_text)
    polarity = analysis.sentiment.polarity


    # determine mood based on polarity
    if polarity > 0.5:
        return "very happy"
    elif polarity > 0:
        return "happy"
    elif polarity == 0:
        return "neutral"
    elif polarity > -0.5:
        return "sad"
    else:
        return "very sad"

