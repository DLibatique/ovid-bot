import random
from os import listdir
from os import path
from os import environ
from cltk.tokenize.line import LineTokenizer
import tweepy
from time import sleep
from apscheduler.schedulers.blocking import BlockingScheduler

#import Twitter credentials
# from credentials import *

# get Twitter creds from Heroku dashboard
consumer_key = environ['CONSUMER_KEY']
consumer_secret = environ['CONSUMER_SECRET']
access_token = environ['ACCESS_KEY']
access_token_secret = environ['ACCESS_SECRET']

#access and authorize Twitter creds
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#initialize tokenizer
tokenizer = LineTokenizer('latin')

#create list of lines
whole_met = []

list_of_files = sorted([file for file in listdir('la') if path.isfile(path.join('la/',file))])

#iterate through files/books of Metamorphoses
for file in list_of_files:

    if file.startswith('ovid'):

        #get text from each file
        with open('la/' + file) as f:
            raw = f.read()

            #add line-tokenized text to the master list of lines
            whole_met += tokenizer.tokenize(raw)

clean_met = [string.replace('\t',' ') for string in whole_met]

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=360)
def tweet_line():
    api.update_status(random.choice(clean_met))

# while whole_met:
#     try:
#         api.update_status(random.choice(clean_met))
#         sleep(21600)
#     except tweepy.TweepError as e:
#         print(e.reason)
