# Import the SentimentIntensityAnalyzer class from the vaderSentiment library.
# This class is used to analyze the sentiment of English texts.
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize the sentiment analyzer.
# This creates an instance of Vader's sentiment analysis tool.
analyzer = SentimentIntensityAnalyzer()

# Define a function to analyze the sentiment of a given text and return a mood classification.
def analyze_sentiment(text: str) -> str:
    """
    Analyze the sentiment of a given text and classify its mood.

    Args:
        text (str): The text to analyze.

    Returns:
        str: The mood of the text, categorized as:
            - "very happy": Highly positive sentiment
            - "happy": Positive sentiment
            - "neutral": Neutral sentiment
            - "sad": Slightly negative sentiment
            - "very sad": Highly negative sentiment
    """
    
    # Use Vader to calculate the compound sentiment score of the text.
    # The 'compound' score is a summary of sentiment ranging from -1 (very negative) to 1 (very positive).
    polarity = analyzer.polarity_scores(text)['compound']
    
    # Classify the mood based on the compound polarity score.
    # Thresholds are defined to distinguish between highly positive, positive, neutral, slightly negative, and highly negative moods.
    if polarity > 0.5:
        return "very happy"  # Strongly positive sentiment
    elif polarity > 0:
        return "happy"  # Positive sentiment
    elif polarity == 0:
        return "neutral"  # Neutral sentiment
    elif polarity > -0.5:
        return "sad"  # Slightly negative sentiment
    else:
        return "very sad"  # Strongly negative sentiment
