# Tweepy-Image-Pull
 A Python script using the Twitter API through tweepy, that will allow you to download an image from Twitter and let's you store it in a destination folder and rename it however you want with only the tweet link.
 Initially made for me to effectively download Gochiusa illustrations for private usage.
 I'm just a beginner and that was one of my first projects, so please go easy on me, if there are any issues.
 
 
# Difference between public.py and newest_post.py
public.py is to download a specific image from a link, that you have copied, whereas newest_post.py will automatically download the image of the newest post of a Twitter profile.

# Requirements
 
 - Twitter Developer App with Keys and Tokens from https://developer.twitter.com/en/apps
 - Python 3.6+

 - pip install tweepy
 - pip install wget
 - pip install pyperclip
 
 - replace variables marked with `<YOUR> `as needed shown in the code 
 
 - if you want to change how the filename is called, change `{url}` in l.84
 
# Usage public.py
 1. Have the tweet link already stored in your clipboard.

 2. Go to the location of the public.py file, open cmd and enter:
 
 ```
 >python public.py 
 ```
 
 3. When asked to continue, copy the link before starting the new downloading process.
 
 # Usage public.py
 2. Go to the location of the public.py file, open cmd and enter:
 
 ```
 >python newest_post.py 
 ```
 
 TIP: Personally, I use a bat file that does that for me as it's quicker.
 
# Links
 Tweepy:      https://www.tweepy.org/  
 Twitter APP: https://developer.twitter.com/en/apps  
 wget:        https://pypi.org/project/wget/  
 pyperclip:   https://pypi.org/project/pyperclip/  
