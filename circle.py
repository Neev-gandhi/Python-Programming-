print("enter the co-ordinates of the center of a circle:")
x=int(input("enter the x co-ordinate of center:"))
y=int(input("enter the y co-ordinate of center:"))

r=int(input("enter the radius of the circle"))

print("entere the point you want to check:")
x1=int(input("enter the x co-ordinate of point:"))
y1=int(input("enter the y co-ordinate of point:"))

d=((x1-x)*(x1-x)+(y1-y)*(y1-y))

if(d>r*r):
    print("it lies outside the circle")
elif(d==r*r):
    print("it lies on the circle")
else:
    print("it lies inside the circle")
