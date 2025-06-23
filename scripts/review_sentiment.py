import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)['compound']
    if score >= 0.05:
        return 'positive', score
    elif score <= -0.05:
        return 'negative', score
    else:
        return 'neutral', score

def process_reviews(csv_input_path, csv_output_path):
    df = pd.read_csv(csv_input_path)
    df[['sentiment', 'polarity_score']] = df['review_text'].apply(
        lambda x: pd.Series(analyze_sentiment(x))
    )
    df.to_csv(csv_output_path, index=False)

if __name__ == "__main__":
    process_reviews("../data/raw/reviews_raw.csv", "../data/processed/sentiment_labeled_reviews.csv")
