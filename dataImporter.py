#import the library to call and read the api, and the library to allow the program to wait.
import requests, time
import thread

#Wunderground has a pretty good documentation on each request type and its results

def getConditions():
    #make some variables global to allow accessing from other functions (this may be removed)
    global apikey, conditions
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
    	#download weather conditions. 
        response = requests.get("http://api.wunderground.com/api/" + apikey + "/conditions/q/autoip.json")
        #read the json file from the request and save the data to conditions object
        conditions = response.json()
	#termTest()
        #TEST: print out the current tempature in f
	#print conditions['current_observation']['temp_f']
	#wait for three minutes, change this if you have a better api plan and request more data. 
        time.sleep(180)
#Run the get conditions function: This will be removed once I in



def getData(section, key):
	return conditions[section][key]

#request data via the terminal
def termTest():
	section = input("catagory: ")
	key = input("key: ")
	print getData(section, key)
try:
    thread.start_new_thread(getConditions, ())
    thread.start_new_thread(termTest, ())
except:
    print "Thread error"

while 1:
    pass
