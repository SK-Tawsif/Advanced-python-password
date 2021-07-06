import random

up_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
low_letter = up_letter.lower()
digits = "0123456789"
symbols = "()@#$%^&*{}[]"

upper, lower , nums , syms = True,True,True,True

all = ""

if upper:
    all += up_letter
if lower:
    all += low_letter
if nums:
    all += digits
if syms:
    all += symbols

length = int(input("Enter the length of passwords: "))    
amount = int(input("Enter the amount of passwords: ")) 

file=open('Database','a')

try:
   for x in range(amount):
                Password = "".join(random.sample(all,length))
                file.write(Password+'\n')
except:
    print("Something went wrong... Please try again")