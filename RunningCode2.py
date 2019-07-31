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

#representing types of chocolate in the box
def cadburyBox(m,w,d):
    print("There are", m, ",", w, ",", d, "in the box")
    
cadburyBox("Milk chocolate", "White chocolate", "Dark chocolate")

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
