n = int(input("Enter the number of raw you want to print : "))

for i in range(n):
    for j in range(i+1):
        print(j+1,end= " ")
    print()