#  Set-Up Process
## Prerequisites
1. Python
1. Selenium
1. Code Editor e.g.  Vs Code 

## Installing Selenium : 
Depending on the version of python your have you can either install it via : for python version 2 `pip install selenium` for python version 3 `pip3 install selenium` . ([Selenium Documentation](https://selenium-python.readthedocs.io/installation.html))


## Installing Chromium Drivers
1. Check your Chrome browser version ( help > About Google Chrome ).
![chrome](https://user-images.githubusercontent.com/42699812/147580414-2d2a06a3-4693-45e9-9e8d-e9d2639c6891.png)

1. Navigate to [chromium drivers](https://chromedriver.chromium.org/home).

1. Select the particular driver version that is similar to your chrome version.
![chromium](https://user-images.githubusercontent.com/42699812/147580585-4ccfad70-8440-42c0-857d-2a813689c4b0.png)

1. Download and extract it . 
![Screenshot at 2021-12-28 18-18-35](https://user-images.githubusercontent.com/42699812/147580804-60fdaf61-dba4-4a78-922e-036bfb50424a.png)

1. Make it executable  `chmod +x chromedriver `
![Screenshot at 2021-12-28 18-22-03](https://user-images.githubusercontent.com/42699812/147581146-0d69944c-9e4d-49d9-a9b2-ee95c5b0c16e.png)

1. Move to a shared folder : `sudo mv chromedriver /usr/local/share/chromedriver`
![Screenshot at 2021-12-28 18-27-17](https://user-images.githubusercontent.com/42699812/147581609-73c4c3a3-1578-4d32-9e20-4e17bcd30deb.png)

1. Link to your bin directory and afterwards confirm if successful by printing out the version of your chromedriver : 
![Screenshot at 2021-12-28 18-31-56](https://user-images.githubusercontent.com/42699812/147582016-65a67199-79a4-4063-a311-9e3946f224d2.png)




# Build Process
1. Create folder , cd to the folder . 
1. Create two python files , secrets.py and appcreate.py
1. Launch Github on browser and create repository for it. 
1. On terminal run : touch .gitignore && echo 'secrets.py' >> .gitignore
 this command will allow you not to push your secrets.py file to git as it will contain your credentials.
1. Proceed with the respective git commands to push the project to github repo. 
1. Proceed to Coding :

## Coding
1.  `secrets.py` Will contain your email address, passowrd and Personal Access Token ( i created one for each project type )

2. `createapp.py` Will contain your operations : 
 
- [x] User to Select which type of app to build
- [x] create directory of particular app in respective project type directory
- [x] Launch Github
- [x] create new repository
- [x] intialize project locally 
- [x] commit and push project to github repo 
- [x] done

The implementation runs cases of VueJS | Flutter | Ardunio 
updates will be made on the Android and Arduino sections. 

Thank you and Happy automation.