i = int(input("Find rev num:"))
rev=0

while(i>0):
    rev = (rev*10)+i%10
    i=i//10
print("reverse is :",rev)
