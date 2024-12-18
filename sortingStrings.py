#sorting array of strings by there lenght:
list=["rajasthan","delhi","goa","utharapradesh","telangana"]
n=len(list)
for i in range(n):
    for j in range(i+1,n):
        if len(list[i])>len(list[j]):
            string=list[i]
            list[i]=list[j]
            list[j]=string
print(list)
