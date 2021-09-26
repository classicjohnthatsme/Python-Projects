import math
print("Enter the height and radius of your cone: ")
height,radius = map(int,input().split())
pi = math.pi
coneArea = pi*radius*(radius+math.sqrt(height**2+radius**2))
print("The area of your cone is: {}".format(coneArea))