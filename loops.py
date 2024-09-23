#!/usr/bin/python3
import random
number = random.randint(-10, 10)
value= ["is zero","is positive","is negative"]

for number in range(-10, 10):
    if number==0:
        print(number,value[0])
      
    elif number>0:
        print(number,value[1])
        
    elif number<0:
        print(number,value[2])