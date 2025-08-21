a=7
b=6
maxv=max(a,b)
while True:
    if maxv%a ==0 and maxv%b==0:
        lcm=maxv
        break
    maxv+=1
print("lcm :",lcm)
