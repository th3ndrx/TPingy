#!/usr/bin/env python
import os, sys, time, tweepy
from datetime import datetime

__author__ =    "Tomislav Sablic"
__copyright__ = "Copyright 2015, Tomislav Sablic"
__license__ =   "MIT"
__version__ =   "1.0"
__email__ =     "tomislav.sablic@outlook.com"
__status__ =    "Development" 

######################## Twitter API auth ##############################
consumer_key    =     'xxxxxxxxxxxxxxxxxxxx'
consumer_secret =     'xxxxxxxxxxxxxxxxxxxx'
access_token    =     'xxxxxxxxxxxxxxxxxxxx'
access_token_secret = 'xxxxxxxxxxxxxxxxxxxx'
appuser =             'xxxxxxxxxxxxxxxxxxxx'
########################################################################

hostname = "nope.gif" # Put your domain here
time_now = datetime.now().strftime('%H:%M')
status = ""
alert = "Something is going on with %s ,you better check it." % hostname

def ping():  
  response = os.system("ping -n 1 " + hostname)
  print "\n" + "-" * 50 + "\n"
  if response == 0:
    print time_now + "\t" + hostname, 'is up!'
    status = 'ok'
    sys.exit()
    print "\n" + "-" * 50 + "\n"    
    time.sleep(300) # Wait for 5 minutes
  else:
    print time_now + "\t" + hostname, 'is down!'
    status = 'error'
    print "\n" + "-" * 50 + "\n"
    TWnotify()
  
    
  
def TWnotify():
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret) # Making a new session
  auth.set_access_token(access_token, access_token_secret)
  api = tweepy.API(auth)
  print "\n" + "+" * 50 + "\n"
  print time_now + "    Successfully logged in as " + api.me().name
  api.send_direct_message(user_id = appuser , text = alert)
  print "\t Message successfully sent."
  print "\n" + "+" * 50 + "\n"
  sys.exit() # Closing the command line, if this script executed locally
  

ping()
while status == 'ok':
  ping()
