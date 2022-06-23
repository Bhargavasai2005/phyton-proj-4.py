# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 21:11:07 2022

@author: ADMIN
"""

def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('mississippi'))