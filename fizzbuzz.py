#!/usr/bin/env python3
def fizzbuzz():
   pass
for i in range(1,101):
    print(i, end=" ")
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    elif i % 3 == 0:
      print("Fizz")

    elif i % 5 == 0:
       print("Buzz")
    