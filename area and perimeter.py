length=int(input("enter the length of the rectangle:"))
breadth=int(input("enter the breadth of the rectangle:"))

area= length*breadth
perimeter=2*(length+breadth)

if(area>perimeter):
    print("area of rectangle is greater than its perimeter")
elif(area==perimeter):
    print("area of rectangle is equal to its perimeter")
else:
    print("area of rectangle is smaller than its perimeter")
