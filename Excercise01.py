#!/usr/bin/python3.5
from datetime import date

def year_when_100():
    name = input("Enter your name:")
    age = int(input("Enter your age:"))

    currentDate = date.today()
    yearWhen100 = currentDate.year + (100 - age)

    print(str(name) + ", you will be 100 years old in " + str(yearWhen100))

