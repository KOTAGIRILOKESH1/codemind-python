n=int(input())
m=0
mm=0
while n>0:
    r=n%10
    if r%2==0:
        m+=1
    else:
        mm+=1
    n=n//10
if m==0:
    print("Odd")
elif mm==0:
    print("Even")
else:
    print("Mixed")