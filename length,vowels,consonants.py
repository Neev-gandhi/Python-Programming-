str=input("enter a string:")
i=0
count=0
x=0
length=len(str)
print(f"the length of the string is:{length}")
for i in range(0,length-1):
    if(str[i] in 'aeiou'):
        count=count+1
    elif(str[i]==' '):
        x=x+1
    i=i+1
print(f"the no.of vowels are :{count}")
print(f"the no.of consonants are:{length-count-x}")