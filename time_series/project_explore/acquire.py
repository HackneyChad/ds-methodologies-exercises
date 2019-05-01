
import pandas as pd
import csv

def merge_dataframes():
    with open('2018-04-26_through_2018-05-26.csv') as fd:
        reader=csv.reader(fd)
        interestingrows=[row for idx, row in enumerate(reader) if idx in range(35,67)]
        df = pd.DataFrame(interestingrows)
    with open('2018-05-27_through_2018-06-26.csv') as fd:
        reader=csv.reader(fd)
        interestingrows=[row for idx, row in enumerate(reader) if idx in range(35,67)]
        df1 = pd.DataFrame(interestingrows)
    with open('2018-06-27_through_2018-07-27.csv') as fd:
        reader=csv.reader(fd)
        interestingrows=[row for idx, row in enumerate(reader) if idx in range(35,67)]
        df2 = pd.DataFrame(interestingrows)
    with open('2018-07-28_through_2018-08-26.csv') as fd:
        reader=csv.reader(fd)
        interestingrows=[row for idx, row in enumerate(reader) if idx in range(34,65)]
        df3 = pd.DataFrame(interestingrows)
    with open('2018-08-27_through_2018-09-26.csv') as fd:
        reader=csv.reader(fd)
        interestingrows=[row for idx, row in enumerate(reader) if idx in range(35,67)]
        df4 = pd.DataFrame(interestingrows)
    with open('2018-09-27_through_2018-10-27.csv') as fd:
        reader=csv.reader(fd)
        interestingrows=[row for idx, row in enumerate(reader) if idx in range(35,67)]
        df5 = pd.DataFrame(interestingrows)
    with open('2018-10-28_through-2018-11-27.csv') as fd:
        reader=csv.reader(fd)
        interestingrows=[row for idx, row in enumerate(reader) if idx in range(35,67)]
        df6 = pd.DataFrame(interestingrows)
    with open('2018-11-28_through_2018-12-28.csv') as fd:
        reader=csv.reader(fd)
        interestingrows=[row for idx, row in enumerate(reader) if idx in range(35,45)]
        df7 = pd.DataFrame(interestingrows)
    frames = [df, df1, df2, df3, df4, df5, df6, df7]
    df = pd.concat(frames)
    df = df.rename(columns={0: "date", 1: 'calories_burned', 2: 'steps', 3: 'distance', 4: ' floors', 5: 'minutes_sedentary', 6: 'minutes_lightly_active',7: 'minutes_fairly_active', 8: 'minutes_very_active',9: 'activity_calories'})
    df.drop([0], inplace=True)
    return df