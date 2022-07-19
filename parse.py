import requests
import pandas as pd
# csv file name
filename = "records.csv"
URL = "https://lichess.org/api/user/"

df = pd.read_csv(filename, keep_default_na=False)

# parse through rows and print column 3
for index, row in df.iterrows():
    if(row[3] != ''):
        r = requests.get(URL + str(row[3])[22:])
        data = r.json()
        if 'perfs' in data:
            if 'storm' in data['perfs']:
                df.at[index, 'No of Puzzle Storms'] = data['perfs']['storm']['runs']
                print(data['perfs']['storm']['runs'])
            if 'playTime' in data:
                df.at[index, 'Playing Time'] = data['playTime']['total']/(60*60)
                print((data['playTime']['total'])/(60*60))

df.to_csv(filename, index=False)