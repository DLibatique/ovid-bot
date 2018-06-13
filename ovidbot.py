import random
from os import listdir
from cltk.tokenize.line import LineTokenizer
import tweepy
from time import sleep

#import Twitter credentials
from credentials import *

#access and authorize Twitter creds
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#initialize tokenizer
tokenizer = LineTokenizer('latin')

#create list of lines
whole_met = []

#iterate through files/books of Metamorphoses
for file in sorted(listdir('ovid_metamorphoses')):

    #get text from each file
    with open('ovid_metamorphoses/' + file) as f:
        raw = f.read()

    #add line-tokenized text to the master list of lines
    whole_met += tokenizer.tokenize(raw)

try:
    api.update_status(random.choice(whole_met))
except tweepy.TweepError as e:
    print(e.reason)

while whole_met:
    api.update_status(random.choice(whole_met))
    sleep(21600)
