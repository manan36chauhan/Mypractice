n = float(input("Enter the number of raw you want to print : "))

for i in range(n):
    for j in range(i,-1,-1):
        print(n-i,end= " ")
    print()