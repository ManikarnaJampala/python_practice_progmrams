#counting the duplicate charecters
string=input("enter a string:")
n=len(string)
for i in range(n):
    count=0
    for j in range(i+1,n):
        if(string[i]==string[j]):
             count=count+1
    print(string[i]+":",count)