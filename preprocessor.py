import pandas as pd

def preprocess(df, region_df):
    # Filtering for summer olympics
    df = df[df['Season'] == 'Summer']
    # Merge with region_df
    df = df.merge(region_df, on='NOC', how='left')
    # Dropping duplicates
    df.drop_duplicates(inplace=True)
    # One-Hot enoding medals
    medal = pd.get_dummies(df['Medal']).astype(int)
    df = pd.concat([df, medal], axis=1)
    return df