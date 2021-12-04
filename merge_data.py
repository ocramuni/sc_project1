#!/bin/env python3

import os 
import json
from jsonmerge import merge

def serialize_json(folder, filename, data):
    if not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
    with open(f"{folder}/{filename}", 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        f.close()
    print(f"Data serialized to path: {folder}/{filename}")

def read_json(path, verbose=True):
    if os.path.exists(path):
        with open(path, "r", encoding="utf8") as file:
            data = json.load(file)
        if verbose:
            print(f"Data read from path: {path}")
        return data
    else:
        print(f"No data found at path: {path}")
        return {}

def add_json_data(accounts):
    for account in accounts:
        username = account['username']
        account['followers'] = read_json(f'data/{username}_followers.json')
        account['following'] = read_json(f'data/{username}_following.json')
        account['tweets'] = read_json(f'data/{username}_tweets.json')


root_accounts = read_json('data/root_level_accounts.json')
add_json_data(root_accounts)

first_level_followers = read_json('data/first_level_followers.json')
add_json_data(first_level_followers)

second_level_followers = read_json('data/second_level_followers.json')
add_json_data(second_level_followers)

followers_merge_result = merge(first_level_followers, second_level_followers)

result = merge(root_accounts, followers_merge_result)

serialize_json('data', 'twitter_data.json', result)
