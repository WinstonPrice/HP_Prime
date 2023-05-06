#PYTHON Inertia
#Python_Inertia
'''Program Overview: 
        1) Ask the user what kind of shape they have
        2) Ask the user what units they are using
        3) Ask the user if their shape is hollow or solid
        4) Promt the user to input their dimentions
        5) Caclulate the second moment of inertias for them 
        '''
        
#Imports 
from math import *

'''Ask the user what kind of shape they have'''
def shape_type():
    print("\n1. Square/Rectangle \n2. Circle \n3. Triangle \n")
    shape = int(input("Enter the corrisponding number for the shape you have: \n"))
    return shape

def hollow_or_solid():
    print("\n1. Hollow \n2. Solid \n")
    hollow = int(input("Enter the corrisponding number for the type of shape you have: \n"))
    return hollow

def units():
    unit = str(input("\nEnter the units that you are using: "))
    return unit

def hollow_square(unit):
    print("\nHollow Square/Rectangle\n")
    a = float(input("Enter the outer width: \n"))
    b = float(input("Enter the outer height: \n"))
    c = float(input("Enter the inner width: \n"))
    d = float(input("Enter the inner height: \n"))
    Ix = (a*b**3 - c*d**3)/12
    Iy = (a**3*b - c**3*d)/12
    print("\nIx = {}{}^4\n".format(Ix, unit))
    print("Iy = {}{}^4\n".format(Iy, unit))
    return Ix, Iy

def solid_square(unit):
    print("Solid Square/Rectangle\n")
    a = float(input("\nEnter the outer width: "))
    b = float(input("\nEnter the outer height: "))
    Ix = a*b**3/12
    Iy = a**3*b/12
    print("\nIx = {}{}^4".format(Ix, unit))
    print("\nIy = {}{}^4\n".format(Iy, unit))
    return Ix, Iy

def hollow_circle(unit):
    print("\nHollow Circle\n")
    r1 = float(input("Enter the outer radius: \n"))
    r2 = float(input("Enter the inner radius: \n"))
    Ix = pi*(r1**4 - r2**4)/4
    Iy = pi*(r1**4 - r2**4)/4
    print("\nIx = {}{}^4".format(Ix, unit))
    print("\nIy = {}{}^4\n".format(Iy, unit))
    return Ix, Iy

def solid_circle(unit):
    print("\nSolid Circle\n")
    r = float(input("\nEnter the radius: "))
    Ix = pi*r**4/4
    Iy = pi*r**4/4
    print("\nIx = {}{}^4\n".format(Ix, unit))
    print("\nIy = {}{}^4\n".format(Iy, unit))
    return Ix, Iy

def solid_triangle(unit):
    print("Solid Triangle\n")
    a = float(input("\nEnter the base: "))
    b = float(input("\nEnter the height:"))
    Ix = a*b**3/36
    Iy = a**3*b/36
    print("\nIx = {}{}^4".format(Ix, unit))
    print("\nIy = {}{}^4".format(Iy, unit))
    return Ix, Iy

def hollow_triangle(unit):
    print("Hollow Triangle\n")
    a = float(input("\nEnter the outer base: "))
    b = float(input("\nEnter the outer height: "))
    c = float(input("\nEnter the inner base: "))
    d = float(input("\nEnter the inner height: "))
    Ix = (a*b**3 - c*d**3)/36
    Iy = (a**3*b - c**3*d)/36
    print("\nIx = {}{}^4".format(Ix, unit))
    print("\nIy = {}{}^4".format(Iy, unit))
    return Ix, Iy

def main():
    shape = shape_type()
    hollow = hollow_or_solid()
    unit = units()
    if shape == 1:
        if hollow == 1:
            hollow_square(unit)
        else:
            solid_square(unit)
    elif shape == 2:
        if hollow == 1:
            hollow_circle(unit)
        else:
            solid_circle(unit)
    else:
        if hollow == 1:
            hollow_triangle(unit)
        else: 
            solid_triangle(unit)
    return

if __name__ == main():
    main()

#end


EXPORT Python_Inertia()

BEGIN
PRINT();
PYTHON(Inertia)
END;
