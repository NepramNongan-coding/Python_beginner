"""basic_maths Module
This module is made by Nongan Nepram on May 13th,2026.This module contains basic arithmetics operations that can be carried out on numbers."""
def addnum(x,y):
    return(x+y)
def subnum(x,y):
    return(x-y)
def multnum(x,y):
    return(x*y)
def divnum(x,y):
    if y ==0:
        print("Division by 0 is wrong")
    else:
        return(x/y)