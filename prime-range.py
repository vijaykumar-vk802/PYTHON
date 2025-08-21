print("Enter the two numbers to check prime or not (range-ex:10-20..)")
a=int(input("Enter lower number:"))
c=int(input("Enter upper number:"))
for j in range(a,c):
   b=''
   for i in range(2,j):
      if j%i==0:
        b="not is a prime"
        break
      else:
        b="is a prime."
   print(f"{j}",b)
        
    
    
