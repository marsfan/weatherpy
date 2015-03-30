import urllib2, json

apikey = xxxxxxxxxxxxxxxx //Enter the API key here, get one for free at api.wunderground.com
dataType = "Conditions"
state = "Tx"
city = "Dallas"

def getData():
    request = urllib2.Request("
