#!/usr/bin/env python3
import calendar
import datetime
import time
from datetime import datetime
from datetime import date

def inputDate():
    '''Input the date for search'''
    sDate=input("Please enter the date in which the flights are to be searched [DD-MM-YYYY]:")
    format='%d-%m-%Y'
    try:
        sDate=datetime.strptime(sDate,format)
    except:
        print("Date is not in desired format [DD-MM-YYYY]")
        contInput()
    day=sDate.day
    monthNum=str(sDate.month)
    datetime_object = datetime.strptime(monthNum, "%m")
    month_name = datetime_object.strftime("%b")
    year=sDate.year
    today=datetime.today()
    if sDate < today:
        print("Selected a future date for booking.")
        contInput()
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
    #day=f"{day:02d}"
    #monthNum=f"{int(monthNum):02d}"
    return str(day), str(monthNum), str(year)

def contInput():
    '''Check to Continue'''
    contInput=input("Press [c/C] to continue or [q/Q] to exit or [r/R] to reneter the date:")
    contIn=str(contInput)
    if (contIn=='q' or contIn=='Q'):
        exit()
    else:
        if (contIn=='r' or contIn=='R'):
            inputDate()
        else:
            if (contIn=='c' or contIn=='C'):
                return
            else:
                try:
                   contInput()
                except:
                    contInput()

def main():
        cDate,cMonth,Year=inputDate()
        print (cDate)
        

#Invoke main function
if __name__=="__main__":
    main()