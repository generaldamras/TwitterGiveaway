# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 22:12:56 2018

@author: Sarmad
"""

# Assume you already have a consumer key and secret from the Twitter app
# ckey
# csecret

from twython import Twython

twitter = Twython(ckey, csecret)

auth = twitter.get_authentication_tokens()
OAUTH_TOKEN = auth['oauth_token']
OAUTH_TOKEN_SECRET = auth['oauth_token_secret']

rts = twitter.get_retweets(id='1044738333111451648')

import urllib.request
import re

def get_user_ids_of_post_likes(post_id):
    try:
        json_data = urllib.request.urlopen('https://twitter.com/i/activity/favorited_popup?id=' + str(post_id)).read()
        found_ids = re.findall(r'data-user-id=\\"+\d+', json_data.decode("utf8"))
        unique_ids = list(set([re.findall(r'\d+', match)[0] for match in found_ids]))
        return unique_ids
    except urllib.request.HTTPError:
        return False
    
users_rt = [(user['user']['name'],user['user']['screen_name']) for user in rts]
users_liked_ids = [twitter.lookup_user(user_id=user_id) for user_id in get_user_ids_of_post_likes(1044738333111451648)]
users_liked = [(a[0]['name'],a[0]['screen_name']) for a in users_liked_ids]

dg_id = twitter.lookup_user(screen_name='DesiticGaming')[0]['id']