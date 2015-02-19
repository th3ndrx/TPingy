#!/usr/bin/env python
import os, sys, time, tweepy
import config
from datetime import datetime

__author__ =    "Tomislav Sablic"
__copyright__ = "Copyright 2015, Tomislav Sablic"
__license__ =   "MIT"
__version__ =   "1.0"
__email__ =     "tomislav.sablic@outlook.com"
__status__ =    "Development" 

hostname = config.hostname
time_now = datetime.now().strftime('%H:%M')
status = ""
alert = config.alert

def sleep(x):
  time.sleep(x*60)

def ping():
  print "Checking for website availability..."
  response = os.system("ping -n 1 " + hostname)
  print "\n" + "-" * 50 + "\n"
  if response == 0:
    print time_now + "\t" + hostname, 'is up!'
    status = 'ok'
    sys.exit()
    print "\n" + "-" * 50 + "\n"    
    sleep(1) # Wait for 5 minutes
  else:
    print time_now + "\t" + hostname, 'is down!'
    status = 'error'
    print "\n" + "-" * 50 + "\n"
    TWnotify()
    continue_operation = raw_input("Do you want to continue monitoring? (y/n): ")
    continue_operation.upper()
    
  
def TWnotify():
  auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret) # Making a new session
  auth.set_access_token(config.access_token, config.access_token_secret)
  api = tweepy.API(auth)
  print "\n" + "+" * 50 + "\n"
  print time_now + "    Successfully logged in as " + api.me().name
  api.send_direct_message(user_id = config.appuser , text = alert)
  print "\t Message successfully sent."
  print "\n" + "+" * 50 + "\n"
  status = "ok"
  #sys.exit() # Closing the command line, if this script executed locally
  

ping()

while status == 'ok':
  if continue_operation == "N": break
  ping()
