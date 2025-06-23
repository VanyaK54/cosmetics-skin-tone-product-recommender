import pandas as pd

def match_products(user_skin_tone, sentiment_df, catalog_df):
    # Filter products with positive sentiment and map to user skin tone
    sentiment_filtered = sentiment_df[sentiment_df['sentiment'] == 'positive']
    merged = sentiment_filtered.merge(catalog_df, on='product_id')
    
    # Dummy logic – In real scenario, add skin-tone compatibility lookup
    top_products = merged.groupby('user_id')['product_id'].apply(list).reset_index()
    top_products.columns = ['user_id', 'top_positive_product_ids']
    return top_products

def generate_recommendations():
    skin_df = pd.read_csv("../data/processed/skin_tone_labels.csv")
    sentiment_df = pd.read_csv("../data/processed/sentiment_labeled_reviews.csv")
    catalog_df = pd.read_csv("../data/raw/product_catalog.csv")

    top_matches = match_products("all", sentiment_df, catalog_df)
    df = pd.merge(skin_df, top_matches, on='user_id', how='left')
    df.to_csv("../data/processed/product_match_dataset.csv", index=False)

if __name__ == "__main__":
    generate_recommendations()
