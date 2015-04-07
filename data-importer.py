import urllib2, json, time

apikey = "xxxxxxxxxxxxx" #Enter the API key here, get one for free at wunderground.com/api
dataType = "Conditions"
state = "TX"
city = "Dallas"
settings = "lang:EN/pws:1/bestfct:1"

#standard format for url is api.wunderground.com/api/"API KEY"/"FEATURES"/"SETTINGS"/q/"QUERY.format.
#API KEY is the api key that you got on the wunderground website.
#FEATURES is the data features that one can request. See documentation on the wunderground site for a list of all features
#Settings is optional, defines some settings: Language, use of Personal Weather stations, Use of wunderground best forcast.
#See the Documentation for more features
#Query is the location: avaible as USStateCode/City, Zip code, Country/City, Lattitude, Longitude, airport code, pws:ID,
#autoip, specific ip. See documentation for a better format guild
#FORMAT is the output format of the file, is eather JSON or XML

def getConditions():
    while True:
    	#set the url for the wunderground api data. The apikey variable in the middle references the key that was entered earlier.
        request = urllib2.Request("http://api.wunderground.com/api/" + apikey + "/conditions/q/autoip.json")
        #download the data requested by teh previous line
        response = urllib2.urlopen(request)
        #read the json file from the request and save the data to conditions object
        conditions = json.load(response)
        #TODO: Add extraction and labeling process
        #TEST: extract the data keys found in the conditions object. 
	print conditions.keys()
	#wait for three minutes, change this if you have a better api plan and request more data. 
        time.sleep(180)
#Run the get conditions function: This will be removed once I in
getConditions()
