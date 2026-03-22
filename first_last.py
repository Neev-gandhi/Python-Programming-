str=input("Enter a string:")
length=len(str)
y=(length//2)-1
print(f"the first character of the string is {str[0]}")
print(f"the last character of the string is {str[length-1]}")
if(length%2==0):
    print(f"there are two middle elements as there are even number of elements in string:{str[y]}{str[length//2]}")
else:
    print(f"the middle element is {str[length//2]}")