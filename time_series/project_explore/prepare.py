import pandas as pd

def update_dtypes(df):
    df['date'] = pd.to_datetime(df.date)
    df['calories_burned'] = df['calories_burned'].str.replace(',', '')
    df['calories_burned'] = df['calories_burned'].astype(int)
    df['steps'] = df['steps'].str.replace(',', '')
    df['steps'] = df['steps'].astype(int)
    df['minutes_sedentary'] = df['minutes_sedentary'].str.replace(',', '')
    df['minutes_sedentary'] = df['minutes_sedentary'].astype(int)
    df['activity_calories'] = df['activity_calories'].str.replace(',', '')
    df['activity_calories'] = df['activity_calories'].astype(int)
    df['distance'] = df['distance'].astype(float)
    df['minutes_lightly_active'] = df['minutes_lightly_active'].astype(int)
    df['minutes_fairly_active'] = df['minutes_fairly_active'].astype(int)
    df['minutes_very_active'] = df['minutes_very_active'].astype(int)
    df[' floors'] = df[' floors'].astype(int)
    df.set_index('date', inplace=True)
    return df




