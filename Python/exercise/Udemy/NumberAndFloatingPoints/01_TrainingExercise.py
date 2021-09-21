#!/usr/bin/env python3

''' Requirement
Let's assume you are planning to use your Python skills to build a social networking service.
You decide to host your application on servers running in the cloud. You pick a hosting provider
that charges $0.51 per hour. You will launch your service using one server and want to know
how much it will cost to operate per day and per month.
Write a Python program that displays the answers to the following questions:
How much does it cost to operate one server per day?
How much does it cost to operate one server per month? '''

charges = 0.51
servers = input('How many servers are you trying to deploy:')
cost_day = 0.51 * 24;
cost_month = 0.51 * ( 24 * 30 );
print('Cost for operating ', servers, 'server for a day   : ', cost_day);
print('Cost for operating ', servers, 'server for a month : ', cost_month);
