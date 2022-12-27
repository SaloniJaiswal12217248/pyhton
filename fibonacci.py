n=int(input("Enter number of terms in the fibonacci series"))
a=1
b=1
c=0
print(a)
print(b)
for i in range(2,n):
    c=a+b
    a=b 
    b=c
    print(c)