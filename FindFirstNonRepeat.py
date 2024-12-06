#finding first non repeated char
string=input("enter a string:")
n=len(string)
for i in range(n):
    count=0
    for j in range(i+1,n):
        if(string[i]==string[j]):
             count=count+1
    if count==0: 
        break
print(string[i]+":",count)