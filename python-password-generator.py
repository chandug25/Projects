import string
import random
password=[]
alphabets=list(string.ascii_letters)
print(alphabets)
digits=["0","1","2","3","4","5","6","7","8","9"]
sym= ["!","@","#","$","%","^"]
print("Welcome to the PyPassword Generator !")
letters=int(input("How many letters would you like to have in your password: "))
numbers=int(input("How many numbers would you like to have in your password: "))
symbols=int(input("How many symbols would you like to have in your password: "))
for i in range(0,letters):
  password+=random.choice(alphabets)
for i in range(0,numbers):
  password+=random.choice(digits)
for i in range(0,symbols):
  password+=random.choice(sym)
print(password)
random.shuffle(password)
print(password)
pass_str=""
for i in range(0,len(password)):
  pass_str+=password[i]
print(pass_str)       