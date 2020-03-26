print('Welcome to my basic calculator for area of a circle')

from math import pi

r = float(input ("Kindly input the radius of your circle : "))

print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))