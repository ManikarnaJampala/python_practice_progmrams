left=111
right=121
list=[]
for i in range(left,right+1):
    j=i
    count=0
    string=str(i)
    length=len(string)
    while i>0:
        n=i%10
        if n==0:
            break
        elif (j%n==0):
            count=count+1
        else:
            break
        i=i//10
    if count==length:
        list.append(j)
print(list)
        