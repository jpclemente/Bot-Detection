import pandas as pd
import numpy as np
import os
import json

with open("./user_types.json") as json_file:
    user_types = json.load(json_file)

root_dir = './data/cresci-2015.csv/'
dirs = sorted(os.listdir(root_dir))

df_users = pd.DataFrame()
df_tweets = pd.DataFrame()
df_friends = pd.DataFrame()
df_followers = pd.DataFrame()

for item in dirs:
    if os.path.isdir(root_dir + item):
        with open(root_dir + item + '/users.csv', 'rb') as users_file:
            is_bot = 1 if item in ['INT.csv', 'FSF.csv', 'TWT.csv'] else 0
            print(item + ': ' + str(is_bot))
            new_data = pd.read_csv(users_file)
            new_data['bot'] = is_bot
            df_users = pd.concat([df_users, new_data])
            
#        with open(root_dir + item + '/tweets.csv', 'rb') as tweets_file:
#            df_tweets = pd.concat([df_tweets, pd.read_csv(tweets_file)])
#            
#        with open(root_dir + item + '/friends.csv', 'rb') as friends_file:
#            df_friends = pd.concat([df_friends, pd.read_csv(friends_file)])
#            
#        with open(root_dir + item + '/followers.csv', 'rb') as followers_file:
#            df_followers = pd.concat([df_followers, pd.read_csv(followers_file)])

def to_bool(df, var):
    df[var] = pd.to_numeric(df[var]).fillna(0)
    df[var] = df[var].astype('bool')
    return df
bool_vars = ['geo_enabled', 'profile_use_background_image']
for var in bool_vars:
    df_users = to_bool(df_users, var)

print(df_users.dtypes)