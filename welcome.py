# Let's create database for Gemini Housing Society.

print("**** Welcome to Grand Bay Database ****")

access = input("Do you want to update the database?")

''' Permission for the accessing database '''
if access != "yes" and access != "Yes":
    exit()


''' Writing in CSV File'''
from society import s1
from fnames import f1
from lnames import l1
from wingnames import w1
from floornumbers import f2
from flatnumbers import f3

class Customer:
    with open('gb.csv', 'w+') as file:

        file.write(s1)
        file.write(f1)
        file.write(l1)
        file.write(w1)
        file.write(f2)
        file.write(f3)
        file.close()


