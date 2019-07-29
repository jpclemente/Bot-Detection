import pandas as pd

with open('./data/cresci-2017.csv/datasets_full.csv/traditional_spambots_1.csv/tweets.csv', 'rb') as file:
    social_spambots_1_users = pd.DataFrame(file)

print(social_spambots_1_users['user_id'].unique())