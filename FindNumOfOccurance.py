# Find the occurances of a given character
inputString=input("enter the string u want:")
inputChar=input("enter any letter from the above string:")
n=len(inputString)
count=0
for i in range(n):
    if inputString[i]==inputChar:
        count=count+1
print(count)