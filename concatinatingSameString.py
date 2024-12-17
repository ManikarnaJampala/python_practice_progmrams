#concatinating the same string n number of times:
string=input("enter a string:")
n=int(input("entr the number of concatinations:"))
new_string=string
i=1
while i<=n:
    new_string=new_string+" "+string
    i=i+1
print(new_string)

