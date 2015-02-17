# TPingy

A simple tool sends you direct message to your Twitter account when your site is offline.
You can either send yourself DM or you can make a new TW account for your app.

### Dependencies

It uses tweepy API for Twitter which you can install from pip:
  
  <code>pip install tweepy </code>
  
### Permissions 

Your Twitter App needs to have Read and write permissions!
  
### config.py

Stores all the data that this script needs to work. It contains Twitter API keys, your hostname and message.

It looks like this:

```
######################## Twitter API auth ###################################
consumer_key    =     'XXXXXXXXXXXXXXXXXX'
consumer_secret =     'XXXXXXXXXXXXXXXXXX'
access_token    =     'XXXXXXXXXXXXXXXXXX'
access_token_secret = 'XXXXXXXXXXXXXXXXXX'
appuser =             'XXXXXXXXXXXXXXXXXX' # ID of the person you will contact
##############################################################################¸


hostname = "XXXXXXXXXXXXXXXXXX" # put your hostname here (e.g. google.com)
alert    = "There is something going on with %s , you should check it." % hostname  # message the app will send
```


Save it as <code>config.py</code> and run <code>TPingy.py</code>
  
