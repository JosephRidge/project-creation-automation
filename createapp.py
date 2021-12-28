import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

name = " Mr. Joseph Ridge. "
def mainApp():
    print("\n*************** Let's Keep Building ! Great Work Jay R ! *************** \n")
    startAppQuestion = input("Would you like to create an app ? (y/n)  ")
    if (startAppQuestion == "y" or startAppQuestion == "Y" or  startAppQuestion =="yes"):
        print("\nYasssss lets do this ..... ")
        os.chdir("/home/ridge/Documents")     
        print("\n_______________________________________\n")
        print("           Available Platforms \n_______________________________________\n \n 1. Vue3 Web Application. \n 2. Flutter Application. \n 3. Android Application. \n 4. Hardware Project (Arduino/ Platfrom.io etc) ")
        choosePlatformToUse = input("\nUnder Which technology would you like to create your platform with ? (1,2,3 or 4)  ")
        return choosePlatformToUse
    else:
        print("Thank you for your time , bye! ")
        exit()
 
def githubOperation():
    print("setting up github .. ")
    driver = webdriver.Chrome(executable_path ='/usr/bin/chromedriver')
    driver.get("http://www.python.org")
    # os.system("git init")
    # os.system("git add .")
    # os.system("git commit -M 'A Step To Greatness With the First Commit'")
    # os.system("npm init vite@latest")

def createVue3App():
    print("\n........................................\n")
    os.chdir("/home/ridge/Documents/Web Development") 
    print(os.getcwd())
    # os.system("npm init vite@latest")
    # projectName = input("kindly input your new project name : ( the one prompted by vue ")
    # os.chdir(f"/home/ridge/Documents/Web Development/{projectName}")
    # print(os.getcwd())
    githubOperation()
    print("Vue3 App created and updated to the github Repo !! ")
    print("\n........................................\n")

def createFlutterApp():
    print("\n........................................\n")
    os.chdir("/home/ridge/Documents/Mobile Development") 
    print(os.getcwd())
    print("Flutter here we go  ......")
    print("\n........................................\n")

def createHardwareProject():
    print("\n........................................\n")
    os.chdir("/home/ridge/Documents/Hardware Development") 
    print(os.getcwd())
    print("Lets Arduino it Baaaby !!")  
    print("\n........................................\n")

def createAndroidApp():
    print("\n........................................\n")
    os.chdir("/home/ridge/Documents/Mobile Development") 
    print(os.getcwd())
    print("Arctic Fox here we come  ......")    
    print("\n........................................\n")      
   
def selectedItem(item):
    print(f"Item selected was : {item}")
    if item == "1":
        createVue3App()
    elif item == "2":
        createFlutterApp()    
    elif item == "3":
        createAndroidApp()
    elif item == "4":
        createHardwareProject()  
    else:
        print("Invalid Selection .. Select valid choice of either 1,2,3 or 4...\n")
        return "0"
        

if (selectedItem(mainApp()) == "0"):
    selectedItem(mainApp())
else:
    print(f"\n Thank you {name}\n")    
    



