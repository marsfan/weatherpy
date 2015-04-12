import requests, time

#Wunderground also has a pretty good documentation on each request type and its results



def getConditions():
    #make some variables global to allow accessing from other functionschrom
    global apikey
    #set the name of the file with the api key
    apifile = open("api.cfg")
    #save api key to a variable
    apikey = apifile.read()
    #close the file to allow it to be accessed by other progams
    apifile.close()
    #loop endlessly so that we can keep getting data
    #TODO: replace this with something that makes it eaiser for
    #other scripts to terminate the process
    while True:
    	#download weather conditions. 
        response = requests.get("http://api.wunderground.com/api/" + apikey + "/conditions/q/autoip.json")
        #read the json file from the request and save the data to conditions object
        conditions = response.json()
        #TEST: print out the current tempature in f
	print conditions['current_observation']['temp_f']
	#wait for three minutes, change this if you have a better api plan and request more data. 
        time.sleep(180)
#Run the get conditions function: This will be removed once I in
getConditions()


#TODO: Finish extraction process
def getData(section, key):
	return conditions['curr
