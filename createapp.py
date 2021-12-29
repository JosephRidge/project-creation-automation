import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import secrets

name = " Mr. Joseph Ridge. "
def mainApp():
    print("\n*************** Let's Keep Building ! Great Work Jay R ! *************** \n")
    startAppQuestion = input("Would you like to create an app ? (y/n)  ")
    if (startAppQuestion == "y" or startAppQuestion == "Y" or  startAppQuestion =="yes"):
        print("\nYasssss lets do this ..... ")
    #     newGithubRepoName = input("Kindly Enter your Repository Name : ")
    #     newGithubRepoDescription = input("Kindly Enter your Project Description ( Brief ): ")
    #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #     driver.get("https://github.com/login")
    #     # inputElement = driver.find_element_by_id("a1")
    #     # inputElement.send_keys('1')
    #     # print(secrets.myPassword)
    #     myGithubEmail = driver.find_element(By.XPATH,'//*[@id="login_field"]')    
    #     myGithubEmail.send_keys(secrets.myEmail)
    #     myGithubPass = driver.find_element(By.XPATH,'//*[@id="password"]')    
    #     myGithubPass.send_keys(secrets.myPassword)
    #     myGithubButton = driver.find_element(By.XPATH,'//*[@id="login"]/div[4]/form/div/input[12]') 
    #     myGithubButton.click()
    # # new repo
    #     driver.get("https://github.com/new")
    #     newGithubRepositoryName = driver.find_element(By.XPATH, '//*[@id="repository_name"]')
    #     newGithubRepositoryName.send_keys(newGithubRepoName)

    #     # newGithubRepositoryDesc = driver.find_element_by_id('repository_description')
    #     # newGithubRepositoryDesc.send_keys(newGithubRepositoryDesc)

    #     repositoryAccessType = driver.find_element(By.XPATH,'//*[@id="repository_visibility_private"]')
    #     repositoryAccessType.click()

    #     createGithubRepo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="new_repository"]/div[6]/button')))
    #     createGithubRepo.click()
    #     remoteREpoUrl = driver.find_element(By.XPATH, '//*[@id="empty-setup-new-repo-echo"]/span[6]/span')
    #     print(f" \n\n {remoteREpoUrl.text}\n\n")
        os.chdir("/home/ridge/Documents")     
        print("\n_______________________________________\n")
        print("           Available Platforms \n_______________________________________\n \n 1. Vue3 Web Application. \n 2. Flutter Application. \n 3. Android Application. \n 4. Hardware Project (Arduino/ Platfrom.io etc) ")
        choosePlatformToUse = input("\nUnder Which technology would you like to create your platform with ? (1,2,3 or 4)  ")
        return choosePlatformToUse
    else:
        print("Thank you for your time , bye! ")
        exit()
 

def githubAccountVerfication(driver):
    print("\n******************** ENTER GITHUB OTP ********************\n") 
    githubOTPCode = driver.find_element(By.XPATH, '//*[@id="otp"]')
    if(githubOTPCode != None):
        gitOtp = input("Input your OTP code : ")
        githubOTPCode.send_keys(gitOtp)    
        githubOTPButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="login"]/div[3]/form/button')))
        githubOTPButton.click() 
        # newGithubRepositoryName = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.XPATH, '//*[@id="repository_name"]'))
        # newGithubRepositoryName.send_keys(newGithubRepoName)
        

    else:
        print("Proceeding to github repo creation ....")    
    print("\n**********************************************************\n") 



def githubOperation(newGithubRepoName, githubPAT):
    print("setting up github .. ")
    # newGithubRepoName = input("Kindly Enter your Repository Name : ")
    # newGithubRepoDescription = input("Kindly Enter your Project Description ( Brief ): ")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # driver.implicitly_wait(10)
    driver.get("https://github.com/login")
    myGithubEmail = driver.find_element(By.XPATH,'//*[@id="login_field"]')    
    myGithubEmail.send_keys(secrets.myEmail)
    myGithubPass = driver.find_element(By.XPATH,'//*[@id="password"]')    
    myGithubPass.send_keys(secrets.myPassword)
    myGithubButton = driver.find_element(By.XPATH,'//*[@id="login"]/div[4]/form/div/input[12]') 
    myGithubButton.click()
    print(f"==== > URL === > {driver.current_url}")
    if(driver.current_url == "https://github.com/sessions/verified-device"):
        githubAccountVerfication(driver) 
        
        # newGithubRepositoryName = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.XPATH, '//*[@id="repository_name"]'))
        # newGithubRepositoryName.send_keys(newGithubRepoName)
    # driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
    
     # new repo

    driver.execute_script("window.open('about:blank', 'secondtab');")
      # It is switching to second tab now
    driver.switch_to.window("secondtab") 
    driver.get("https://github.com/new")
    # newGithubRepoPage = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.XPATH,'//*[@id="repos-container"]/h2/a'))
    # newGithubRepoPage.click()
  
    repositoryAccessType = driver.find_element(By.XPATH,'//*[@id="repository_visibility_private"]')
    repositoryAccessType.click()
    createGithubRepo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="new_repository"]/div[6]/button')))
    createGithubRepo.click()
    remoteRepoUrl = driver.find_element(By.XPATH, '//*[@id="empty-setup-new-repo-echo"]/span[6]/span')
    print(f" --- >  \n\n {remoteRepoUrl.text}\n\n")
    os.system("git init")
    os.system("git add .")
    os.system("git commit -m 'A Step To Greatness Hence, the First Commit'")
    os.system("git branch -M main")
    os.system(f"git remote add origin {remoteRepoUrl.text}")
    print(f"\n {githubPAT} \n")
    os.system(f"git push -u origin main ") 
    # os.system(secrets.myEmail)

def createVue3App():
    githubPAT = "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"
    print("\n........................................\n")
    os.chdir("/home/ridge/Documents/Web Development") 
    print(os.getcwd())
    print("npm init vite@latest is running ........")
    os.system("npm init vite@latest")
    projectName = input("\nkindly input your new project name : ( the one you set as your new vuew app) :  ")
    os.chdir(f"/home/ridge/Documents/Web Development/{projectName}")
    print(os.getcwd())
    githubOperation(projectName,githubPAT)
    print("Vue3 App created and updated to the github Repo !! ")
    print("\n........................................\n")

def createFlutterApp():
    githubPAT = "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"
    print("\n........................................\n")
    print("Flutter here we go  ......")
    os.chdir("/home/ridge/Documents/Mobile Development") 
    print(os.getcwd())
    newAppName = input("What is the name of your app ? ")    
    os.system(f"flutter create {newAppName}")
    os.chdir(f"/home/ridge/Documents/Mobile Development/{newAppName}")
    githubOperation(newAppName,githubPAT)
    print("Kindly Launch Android Studio and open it from there thank you  ......")    
    print("\n........................................\n")

def createHardwareProject():
    githubPAT = "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"
    print("\n........................................\n")
    print("Lets Arduino it Baaaby !!")  
    os.chdir("/home/ridge/Documents/Hardware Development") 
    newAppName = input("What is the name of your Hardware Project ? ")     
    os.system(f"mkdir {newAppName}")
    os.system(f"cd {newAppName}")
    os.system(f"touch {newAppName}.ino")
    githubOperation(newAppName,githubPAT)
    print(f"Once Arduino Launches navigate to file > open > (/home/ridge/Documents/Hardware Development/{newAppName}))")
    os.system("/home/ridge/Downloads/arduino-1.8.16/arduino")  
    print(os.getcwd())
    print("\n........................................\n")

def createAndroidApp():
    githubPAT = "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"
    print("\n........................................\n")
    print("Arctic Fox here we come  ......")
    os.chdir("/home/ridge/Documents/Mobile Development") 
    print(os.getcwd())    
    print("Kindly Launch Android Studio and create project from there thank you ( remember to set directory as /home/ridge/Documents/Mobile Development )  ......") 
    print(f"\n........................................ * HI {name}, KINDLY NOTE * ........................................\n")   
    print("Kindly note that You will have to launch and intialize app from Android Studio for your Native application..") 
    print(f"\n................... * KINDLY USE THIS AS YOUR PAT : {githubPAT} as you set up Version-Control* ...................\n") 
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
    



