# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file. 
"""
#print ("Hello my name is Saanjh")
#print ("Spyder")

def multiply(a,b):
    multiply = a*b
    
    print (multiply)
    
multiply(4,5)

def sum(a,b):
    sum = a+b
    
    print (sum)
    
sum(4,5)

def area(b,h):
    area = (.5)*b*h
    
    print("The area of the triangle with base", b,"and height", h, "=", area) 
    
area(3,5)

#practice
cadburyBox = 5
cadburyBox = cadburyBox + 10
print(cadburyBox)

def cadburyBox(a):
    cadburyBox = a + 5
    print("You have", cadburyBox, "chocolates")
    
cadburyBox(5)

#new lesson
Cadbury1 = "Milk Chocolate"
Cadbury2 = "Dark Chocolate"
Cadbury3 = "White Chocolate"

print(Cadbury1, Cadbury2, Cadbury3)

Cadburymilk = 6
Cadburydark = 5
Cadburywhite = 8

print(Cadburymilk, Cadburydark, Cadburywhite)

chocolate1 = {Cadbury1: 6}
print(chocolate1)
chocolate2 = {Cadbury2: 5}
print(chocolate2)
chocolate3 = {Cadbury3: 8}
print(chocolate3)

#7/31/19
#using the dict function
Nameage = {"Steve":(32,"Male"), "Lia":(28, "Female"), "Vin":(45,"Male"), "Katie":(38,"Female")}
print(Nameage)

#using lists
studentlist = [["steve", 32, "M"], ["lia", 28, "F"], ["vin", 45, "M"], ["katie", 38, "F"]]
print(studentlist)
#representing types of chocolate in the box
def cadburyBox(m,w,d):
    print("There are", m, ",", w, ",", d, "in the box")
    
cadburyBox("Milk chocolate", "White chocolate", "Dark chocolate")

#new lesson
print('Enter your name:')
x = input()
print('Hello, ' + x)

name = input("Please enter your name")
print("Your name is", name)

ageint = int(age)
ageint

import math
dir(math)
math.pi
math.factorial(0)
math.pow(6,15)
math.pow(4,(1/2))


def cuberoot(a):
    cuberoot = math.pow(a,(1/3))
    print("The cubic root of", a, "is", cuberoot)

cuberoot(27)

print('Enter a value:')
x = int(input())
print('The cubic root of', x, "is", math.pow(x,(1/3)))

#PANDAS USAGE
import pandas
dir(pandas)

studentdf = pandas.DataFrame(studentlist, columns=("name", "age", "gender"))
print(studentdf)

chocolates = [["milk", 5], ["dark", 8], ["white", 3]]
chocodf = pandas.DataFrame(chocolates, columns = ("chocolate", "quantity"))
print(chocodf)
 
#afternoon 
studentdf["name"]
studentdf["age"]

studentdf2 = pandas.DataFrame(studentlist,columns=("name", "age", "gender"), index=["1","2","3","4"])
studentdf2


#plotting the data
import plotly
dir(plotly)

from plotly.offline import plot 
import plotly.graph_objs as go

studentbar = go.Bar(x=studentdf["name"], y=studentdf["age"])
plot([studentbar])

chocobar = go.Bar(x=chocodf["chocolate"], y=chocodf["quantity"])
plot([chocobar])

titles = go.Layout(title = "number of chocolates by type")
chocobar = go.Bar(x=chocodf["chocolate"], y=chocodf["quantity"])
fig = go.Figure(data=[chocobar], layout=titles)
plot(fig)
