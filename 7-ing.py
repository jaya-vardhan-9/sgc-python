n=int(input("enter input n"))
print("enter p and g respectively")
p,g=[int(x) for x in input().split()]
arr=[]
powers=[]
for i in range(n):
    temp=int(input("enter "+ str(i)+" th key"))
    powers.append(temp)
    #zero round
    arr.append(pow(g,temp,p))
for i in range(1,n):

    oldarr=arr[:]
    for j in range(n):
        arr[j]=pow(oldarr[j-1],powers[j],p)


print(arr)


# input format
# enter input n3
# enter p and g respectively
#7 3
# enter 0 th key2
# enter 1 th key3
# enter 2 th key4
