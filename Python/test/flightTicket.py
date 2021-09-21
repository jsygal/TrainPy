#!/usr/bin/env python3

#Import the Selinum Modules for WebScrapping Automation
import selenium
from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#Importing Pands for displaying the dataframes
import pandas as pd
import numpy as np
#Importing for delays and to get current time
import datetime
import time
from datetime import date

#Setting up the chrome driver
driver = wb.Chrome("/usr/local/bin/chromedriver")

def inputDate():
    #Input the date on which cheap flights are available
    sDate=input("Please enter the date n which the flights are available [DD-MM-YYYY]:")
    format='%d-%m-%Y'
    day=datetime.strptime(sDate,'%d')
    month=datetime.strptime(sDate,'%m')
    year=datetime.strptime(sDate,'%Y')
    try:
        sDate=datetime.strptime(sDate,format)
        contFlow=input("The date entered is {}th day of {}th month in {} Year. \nPress [y/Y] to continue or [n/N] to reneter the date:".format(day,month,year));
    except:
        print("The date entered is not in correct format, please reneter the date:")
        inputDate()


month = [1,1,1,1,1,1,1]
month = [str(x).zfill(2) for x in month]
day = [4,5,6,7,8,9,10]
day = [str(x).zfill(2) for x in day]
year = [2021,2021,2021,2021,2021,2021,2021]
year = [str(x).zfill(4) for x in year]


