#BASIC FIRST CODES----------------------------------------------------------------------------------------------------------
import tweepy
from tweepy import OAuthHandler
import json
import wget
import sys

consumer_key = '<YOUR-CONSUMER-KEY>'
consumer_secret = '<YOUR-CONSUMER-SECRET>'
access_token = '<YOUR-ACCESS-TOKEN>'
access_secret = '<YOUR-ACCESS-SECRET>'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

tweets = api.user_timeline(screen_name='<YOUR-TWITTERID>',
                           count=1, include_rts=True,
                           exclude_replies=True)

media_files = ''
expandedurl = ''
for status in tweets:
    #from the list entities get the var media, if not found return [] which is none
    media = status.entities.get('media', [])
    if(len(media) > 0):
        #will add the media_url of medias first variabel to media_files as long media still has variables left
        media_files = (media[0]['media_url'])
        expandedurl = (media[0]['expanded_url'])

file_type = media_files[-3:]
media_files1 = media_files[:-4]
data_type = ''
if file_type == 'jpg':
    raw_url = media_files1 + '?format=jpg&name=orig'
    data_type = 'jpg'
else:
    raw_url = media_files1 + '?format=png&name=orig'
    data_type = 'png'

expandedurl = expandedurl[:-8]
expandedurl = expandedurl.replace(':', '')
expandedurl = expandedurl.replace('/', '')

out = f'<YOUR-OUTPUT-PATH>{expandedurl}.{data_type}'


wget.download(raw_url, out=out)
