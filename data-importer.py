import urllib2, json, time

apikey = "xxxxxxxxxxxxx" #Enter the API key here, get one for free at wunderground.com/api
dataType = "Conditions"
state = "TX"
city = "Dallas"
settings = "lang:EN/pws:1/bestfct:1"

#standard format for url is api.wunderground.com/api/"API KEY"/"FEATURES"/"SETTINGS"/q/"QUERY.format.
#API KEY is teh api key that you got on the wunderground website.
#FEATURES is the data features that one can request. See documentation on the wunderground site for a list of all features
#Settings is optional, defines some settings: Language, use of Personal Weather stations, Use of wunderground best forcast.
#See the Documentation for more features
#Query is the location: avaible as USStateCode/City, Zip code, Country/City, Lattitude, Longitude, airport code, pws:ID,
#autoip, specific ip. See documentation for a better format guild
#FORMAT is the output format of the file, is eather JSON or XML

def getConditions():
    while True:
        request = urllib2.Request("http://api.wunderground.com/api/" + apikey + "/conditions/q/autoip.json")
        conditions = urllib2.urlopen(request)
        parseddata = json.load(conditions)
        #TODO: Add extraction and labeling process
	print time.localtime()
        time.sleep(180)

getConditions()
