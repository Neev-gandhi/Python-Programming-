x1=int(input("enter x1:"))
y1=int(input("enter y1:"))
x2=int(input("enter x2:"))
y2=int(input("enter y2:"))
x3=int(input("enter x3:"))
y3=int(input("enter y3:"))

m1=(y2-y1)/(x2-x1)
m2=(y3-y2)/(x3-x2)

if(x2-x1==0 or x3-x2==0):
    print("error")
if(m1==m2):
    print("the points lie on a straight line")
else:
    print("the points does not lie on a straight line ")
