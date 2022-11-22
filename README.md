# Technometrics Task
This project is an assesment task for the "Technometrics LTD".

Task completed by:  **Abdullah Al-Mamun**

**[This configuration is for windows only and it must have Chrome Browser]**

## Prerequisites

1. Install python in your machine.

    -- Try to install Python version 3 at least, because they comes with pip installed with it otherwise you may need to install pip seperately.

2. Selenium requires a driver to interface with the chosen browser. Based on your browser version choose your browser driver. Here are some
   useful links to get your browser driver.
   
   --  Chrome:	https://sites.google.com/chromium.org/driver/
   
   --  Firefox:	https://github.com/mozilla/geckodriver/releases
   
   --  Edge:	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
   
   --  Safari:	https://webkit.org/blog/6900/webdriver-support-in-safari-10/

[If you don't want to use the driver then you can use selenium server also.]
## How to run the project

* To clone the project type:

    ```git clone https://github.com/mamun-nstu/technometrics_task.git```
    
* Then create a virtual environment by typing:

    ```pip install virtualenv```     (to install venv)
    
    ```virtualenv venv```            (to create venv)
    
    ```venv/Script/activate```      (to activate venv)
    
* Install python dependencies:

    ```pip install -r requirements.txt```
    
* Finally to run the codebase in a code editor open the terminal and run:

    ```python twitter_scrapper.py```
    
* In the console you will be  asked to give the number of tweet required. Just enter the value you need.
