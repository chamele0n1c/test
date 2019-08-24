import mechanize as mech
import bs4
import requests as req
import os
import sys
import web
import pickle
import json
import webbrowser

global tempHTML
tempHTML = ""

def pause():
    os.system("pause")
    os.system("wait 5")
    os.system("cls")



urls = (
  '/passwd', 'getPasswd',
  '/live', 'getLive'
)


br = mech.Browser()
br.add_headers = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36')]
br.set_handle_robots(False)
uri = "https://google.com/"

response = br.open(uri)
webbrowser.open(uri)
tempHTML = response

class getLive:
    def GET(self):
        global tempHTML
        return tempHTML

class getPasswd:
    def GET(self):
        appInst2 = AppCore()
        log("getPasswd (GET) Returning %s" % json.dumps(appInst2.Auth))
        return json.dumps(appInst2.Auth)


def log(stdin):
    print(stdin)
class AppCore:
    global confFile
    global Auth
    confFile = "conf/app.conf"
    Auth = []
    
    def __init__(self):
        if os.path.exists(confFile):
             with open(confFile, 'r+') as file:
                 read = pickle.load(file)
                 self.Auth = read
                 file.close()
                 
        if os.path.exists(confFile) != True:
            self.initDB()
            
    def initDB(self):
        if os.path.exists(confFile):
            pass
        
        else:
            print "Configuration File Not Detected. Initialize?"
            response = raw_input("(Yes, No)-}> ")
            if response.lower() == "yes":
                username = raw_input("New APIUserAuth Username: ")
                pause()
                password = raw_input("New APIUserAuth Password: ")
                pause()
                with open(confFile, 'w+') as file:
                    Auth = {"User": username, "Pass": password}
                    pickle.dump(Auth, file)
                    file.close()
                    self.__init__()
                    
            if response.lower() == "no":
                return()
    def runValidation(self):
        if self.Auth:
            Auth = self.Auth
            print "Detected APIUserAuth User: %s" % Auth['User']
        else:
            print "Failed to Detect APIUserAuth User..."
            sys.exit(1)
            
        




def main():
    global tempHTML
    print "Server Core Starting"
    appInst1 = AppCore()
    appInst1.runValidation()
    print "Executing WebPy Server"
    app = web.application(urls, globals())
    app.run()
   

    

if __name__ == "__main__":   
    main()
    print 'Exited Main Execution Code (0)'
    sys.exit(0)
                    
                    
            
        
