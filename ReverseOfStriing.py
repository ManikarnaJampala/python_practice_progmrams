#reverse of a string
string=input("enter any string:")
#in general way
for i in range(len(string)-1,-1,-1):
    print(string[i],end="")
print()
#with using inbuilt function
print(string[::-1])