i=int(input("Enter number to check wether it is armstrong number or not:"))
orig=i
sum=0

while(i>0):
    sum =sum+(i%10)*(i%10)*(i%10)
    i = i//10

if orig==sum:
    print("Enterd number is armstrong")
else:
    print("Enterd number is not armstrong")
