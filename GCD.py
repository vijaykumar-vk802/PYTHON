print("Enter two numbers to find GCD ")
a=int(input("Number 1:"))
b=int(input("Number 2:"))
while(b!=0):
   rem=a%b
   a=b
   b=rem
print("GCD of two numbers:",a)
