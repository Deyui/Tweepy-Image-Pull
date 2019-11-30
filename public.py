#install tweepy, wget and pyperclip if you don't have them yet
#to be replaced variables are marked with <YOUR> line. 15, 16, 17, 18 and 84
import tweepy
from tweepy import OAuthHandler
import json
import wget
import sys
from sys import argv
import pyperclip
import os
import requests

#Connects your App to the Twitter API
#get them from https://developer.twitter.com/en/apps
consumer_key = '<YOUR-CONSUMER-KEY>'
consumer_secret = '<YOUR-CONSUMER-SECRET>'
access_token = '<YOUR-ACCESS-TOKEN>'
access_secret = '<YOUR-ACCESS-SECRET>'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


# the main script is inside a loop, so it will repeatedly ask you whether you want to continue downloading
def repeat():
    #takes link directly from your clipboard
    link = ''
    link = pyperclip.paste()
    link = link.replace(' ','')

    #if its not a twitter link then it will exit
    if 'twitter' not in link:
        print('This is not a Twitter link.')
        exit(0)

    #if it has this weird device string in front, it will also be removed
    if '?s=' in link:
        url = link[:-5]
    else:
        url = link

    #getting id
    backwards = url[::-1]
    id_backwards = ''

    i = 0

    while backwards[i] != '/':
            id_backwards = id_backwards + backwards[i]
            i += 1
            if backwards[i] == '/':
                break


    id = id_backwards[::-1]

    #removes all dots and slashes since you cannot name your file with those characters on windows
    url = url.replace(':', '')
    url = url.replace('/', '')


    #from the id so we can get the media_url from the status in order to read the filetype and to get the download link
    tweet_IDs = id
    status = ''
    tweets = (api.get_status(tweet_IDs)).entities.get('media', [])
    media_files = (tweets[0]['media_url'])

    #checks jpg or png
    file_type = media_files[-3:]

    #gets download link for either jpg or png
    media_files1 = media_files[:-4]
    data_type = ''
    if file_type == 'jpg':
        raw_url = media_files1 + '?format=jpg&name=orig'
        data_type = 'jpg'
    else:
        raw_url = media_files1 + '?format=png&name=orig'
        data_type = 'png'

    #output path and filename/-type
    out = f'<YOUR-OUTPUT-PATH>{url}.{data_type}'

    try:
        #wget gets download link and output path parameter
        wget.download(raw_url, out=out )
    finally:
        print(f'\nDownload successful!.')

    decision = input('Do you want to continue downloading?\n1.Yes | 2.No\n> ')
    if decision == '1':
        repeat()
    elif decision == '2':
        print('Closing...')
        exit()

    else:
        print('ERROR')
        exit()
repeat()
