# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 15:52:39 2019

@author: AN389897
"""
try:
    input1 = str(int(input('Please input your 20 digit number: ')))

    if len(input1) != 20:
        raise Exception('Number should be of 20 digit')
    else:
        for i in range(2,100):
            input1 = int(input1)
            x = int(input1//i)
            if '4' in str(x):
                continue
            else:
                y = input1 - int(x)
                if '4' in str(y):
                    continue
                else:
                    print(x,y)
                    break
except Exception as e:
    Print(Error occurred: ', e)
