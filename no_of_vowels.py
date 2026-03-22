name=input("enter your name:")
name=name.lower()
count=0

for i in range(0,len(name),1):
    if(name[i] in 'aeiou'):
        count=count+1
print(f"the no.of vowels are {count}")
