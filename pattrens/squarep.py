a=int(input("Enter no. of lines:"))
for i in range (a):
    for j in range (a):
        if j==0 or i==0 or j==a-1 or i==a-1 :
         print("*",end= " ")
        else:
            print(" ",end=" ")
    print()
