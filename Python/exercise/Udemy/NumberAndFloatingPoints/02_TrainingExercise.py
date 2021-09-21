#!/usr/bin/env python3

''' Requirement
Building on the previous example, let's also assume that you have saved $918 to fund your new
adventure. You wonder how many days you can keep one server running before your money
runs out. Of course, you hope your social network becomes popular and requires 20 servers to
keep up with the demand. How much will it cost to operate at that point?
Write a Python program that displays the answers to the following questions:
How much does it cost to operate one server per day?
How much does it cost to operate one server per month?
How much does it cost to operate twenty servers per day?
How much does it cost to operate twenty servers per month?
How many days can I operate one server with $918? '''

charges = 0.51
servers = 1
cost_day = 0.51 * 24;
cost_month = 0.51 * ( 24 * 30 );
print('Cost for operating ', servers,'server for a day   : $',cost_day);
print('Cost for operating ', servers,'server for a month : $',cost_month);
servers=20;
print('Cost for operating ', servers,'servers for a day  : $',(servers*cost_day));
print('Cost for operating ', servers, 'servers for a month: $',(servers*cost_month))


