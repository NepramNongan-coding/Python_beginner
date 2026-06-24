# User defined function
# calculate area, perimeter, surface area
# shapes - square, rectangle, triangle, circle, cylinder
# func(param) return calculated value
# module import is allowed

def areaSqua(a):
    return a**2

def areaRect(l, b):
    return l*b

def areaTria(b,h):
    return (1/2)*b*h

def areaCirc(r):
    return (3.14)*(r**2)

def periSqua(a):
    return 4*a

def periRect(l,b):
    return 2*(l+b)

def periTria(l,b,h):
    return l+b+h

def periCirc(r):
    return 2*3.14*r

def surfareaCyli(r,h):
    return 2*3.14*r*(r+h)

print("1.Square")
print("2.Rectangle")
print("3.Triangle")
print("4.Circle")
print("5.Cylinder")

choice = input("Enter the option from the given:")

if choice == "1":
    a = int(input("Enter the length of the side of the square:"))
    print("The area of the square is ", areaSqua(a))
    print("The perimeter of the square is ", periSqua(a))

elif choice == "2":
    l = int(input("Enter the length of the rectangle:"))
    b = int(input("Enter the breadth of the rectangle:"))
    print("The area of the rectangle is", areaRect(l,b))
    print("The perimeter of the rectangle is", periRect(l,b))

elif choice == "3":
    l = int(input("Enter the length of the triangle:"))
    b = int(input("Enter the base of the triangle:"))
    h = int(input("Enter the height of the triangle :"))
    print("The area of the triangle is",areaTria(b,h))
    print("The perimeter of the circle is",periTria(l,b,h))

elif choice == "4":
    r = int(input("Enter the radius of the circle:"))
    print("The area of the circle is",areaCirc(r))
    print("The circumference of the circle is",periCirc(r))

elif choice == "5":
    r = int(input("Enter the radius of the cylinder:"))
    h = int(input("Enter the height of the cylinder :"))
    print("The surface area of the cylinder is",surfareaCyli(r,h))

else: 
    print("Invalid option please try again")