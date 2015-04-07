import requests, time

apikey = "f44871320bb6dd2f" #Enter the API key here, get one for free at wunderground.com/api
#Wunderground also has a pretty good documentation on each request type and its results



def getConditions():
    while True:
    	#set the url for the wunderground api data. The apikey variable in the middle references the key that was entered earlier.
        response = requests.get("http://api.wunderground.com/api/" + apikey + "/conditions/q/autoip.json")
        #read the json file from the request and save the data to conditions object
        conditions = response.json()
        #TODO: Add extraction and labeling process
        #TEST: print out the keys for the current observation data.
	print conditions['current_observation'].keys()
	#wait for three minutes, change this if you have a better api plan and request more data. 
        time.sleep(180)
#Run the get conditions function: This will be removed once I in
getConditions()
