x=input("enter a string:")
length=len(x)
i=0
print("The String in forward order is:")
while(i<length):
    print(x[i])
    i=i+1

print("The String in reversed order is:")
j=length-1
while(j>=0):
    print(x[j])
    j=j-1
    