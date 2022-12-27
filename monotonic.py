a=[]
n=int(input("Enter number of elements in array"))
print("Enter values in array of size ",n)
for i in range(n):
    m=int(input())
    a.append(m)

c1=c2=0
a.append(0)
for i in range(n-1):
    if(a[i]>a[i+1]):
        c1+=1
    if(a[i]<a[i+1]):
        c2+=1

if(c1==0 or c2==0):
    print(" Monotonic")
    if((c1==0)):
        print("Increasing")
    elif(c2==0):
        print("Decreasing")
else:
    print("Not monotonic")

