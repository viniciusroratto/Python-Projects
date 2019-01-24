# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 20:52:34 2019

@author: vinic
"""

import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower( )
    
    if word in data:
        return data[word]
    
    elif (len(get_close_matches(word, data.keys())) > 0 ):
         yn = input("did you mean %s instead? Press Y if yes or N if not: " % get_close_matches(word, data.keys())[0])
         if yn.upper() == "Y":
             return data[ get_close_matches(word, data.keys())[0]]
         elif yn.upper() == "N":
             return "wrong word"
         else:
             return "we didn't understand your querry"
    else:
       return("wrong word")

word = input("enter word: ")

output = translate(word)

if type(output) is list:
    for item in output:
        print (item)
else:
    print(item)