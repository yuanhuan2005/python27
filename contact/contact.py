#!/usr/bin/env python
#coding:utf8
#Author:zhuima
#Email:993182876@qq.com
#Date:2015-03-23
#Function:Create the address book step by step
#Version:0.1

#Initialized variables
msg = '''
    1. Add information
    2. Display information
    0. Exit
'''
#txl content like this tex = [['name','gender','telphone'],['name','gender','telphone']]
txl = []
#define Add
#define display
while True:
    print(msg)
    op = raw_input('Please Select >>> ')
    if op == '1':
        name = raw_input('Please Enter Your name >>> ')
        gender = 0
        while True:
            try:
                gender = int(raw_input('Please Enter Your gender(1 for male, 2 for female) >>> '))
                if gender in [1,2]:
                    break
                else:
                    print("Oops! not in range. Try again...")
            except ValueError as var:
                print("Oops! That was no valid number. Try again...")
                print(var)
        tel = raw_input('Please Enter Your Telphone Number >>> ')
        txl.append([name,gender,tel])
    elif op == '2':
        for list in txl:
           for info in list:
              print(info)
           print("")
    elif op == '0':
        break
    else:
        print("")
        print("Unkonw Choose,Please Select again!")
        print("")