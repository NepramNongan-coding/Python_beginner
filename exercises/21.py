#To compute the height of the wall
import math
length = int(input("Enter the height of the ladder:"))
angle = int(input("Enter the angle in degree formed by the ladder and the ground:"))
height = length*math.sin(math.radians(angle))
print("The height of the wall is", height)