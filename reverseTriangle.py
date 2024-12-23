#printing reverse triange with stars in reguired rows:
n=int(input("enter the number of rows"))
for i in range(n-1,-1,-1):
    for j in range(i):
        print(" ",end="")
    for k in range(n-i):
        print("*",end=" ")
    print()
