#import the library to call and read the api, and the library to allow the program to wait.
import requests, time
import threading

#Wunderground has a pretty good documentation on each request type and its results

def getConditions():
    #make some variables global to allow accessing from other functions (this may be removed)
    global apikey, conditions
    global conditions
    #set the name of the file with the api key and open it. 
    apifile = open("api.cfg")
    #save api key to a variable
    apikey = apifile.read()
    #close the file to allow it to be accessed by other progams
    apifile.close()
    #loop endlessly so that we can keep getting data
    #TODO: replace this with something that makes it eaiser for
    #other scripts to terminate the process
    while True:
        global conditions
    	#download weather conditions. 
        response = requests.get("http://api.wunderground.com/api/" + apikey + "/conditions/q/autoip.json")
        #read the json file from the request and save the data to conditions object
        conditions = response.json()
	#wait for three minutes, change this if you have a better api plan and request more data. 
        time.sleep(180)
#Run the get conditions function: This will be removed once I in



def getData(section, key):
	return conditions

#request data via the terminal
def termTest():
    global conditions
    section = input("catagory: ")
    key = input("key: ")
    print(getData(section, key))

threads = []
data = threading.Thread(target = getConditions, args=())
#term = threading.Thread(target = termTest, args=())
threads.append(data)
#threads.append(term)
data.start()
#term.start()

#while 1:
#    pass
