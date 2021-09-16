#!/usr/bin/env python3
import calendar
import datetime
import time
from datetime import datetime

def inputDate():
    '''Input the date for search'''
    sDate=input("Please enter the date in which the flights are to be searched [DD-MM-YYYY]:")
    format='%d-%m-%Y'
    sDate=datetime.strptime(sDate,format)
    day=sDate.day
    monthNum=str(sDate.month)
    datetime_object = datetime.strptime(monthNum, "%m")
    month_name = datetime_object.strftime("%b")
    year=sDate.year
    chkDay=day%10
    if chkDay==1:
        print("The date entered is {}st day of {} in {}. \n".format(day,month_name,year))
        contInput()
    else:
        if chkDay==2:
            print("The date entered is {}nd day of {} in {}. \n".format(day,month_name,year))
            contInput()
        else:
            if chkDay==3:
                print("The date entered is {}rd day of {} in {}. \n".format(day,month_name,year))
                contInput()
            else:
                print("The date entered is {}th day of {} in {}. \n".format(day,month_name,year))
                contInput()

def contInput():
    '''Check to Continue'''
    contInput=input("Press [y/Y] to continue or [n/N] to reneter the date:")
    contIn=str(contInput)
    if (contIn=='y' or contIn=='Y'):
        exit()
    else:
        if (contIn=='n' or contIn=='N'):
            inputDate()
        else:
            print("Please enter requested reply.\n")
            try:
                contInput()
            except:
                print("Please enter requested reply.\n")
                contInput()

def main():
        inputDate()

#Invoke main function
if __name__=="__main__":
    main()