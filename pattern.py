x=int(input())
y=(x+x-1)-1
index=y//2
mid=y//2
for i in range(x):
    if i%2==0:
        print(" "*index)
        for j in range(index,mid+1):
            if j%2==0:
                print("x")
            else:
                print(" ")
    else:
        continue