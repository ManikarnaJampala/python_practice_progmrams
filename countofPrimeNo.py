n=int(input("enter an number"))
count=0
if n==0 or n==1:
    print(0)
        #else:
for i in range(2,n):
    add=0
    for j in range(1,i+1):
        if i%j==0:
            add=add+1
    if add==2:
            count=count+1
              
print(count)