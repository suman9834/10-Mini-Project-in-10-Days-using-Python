# 10 Mini Project in 10 Days # Project 3 username generator
import random

name = input("Enter your name: ")

numbers = str(random.randint(10,999))

symbols = [ "_", "." , ""]

username = name.lower() + random.choice(symbols) + numbers

print("Your generated username is: ", username)