import math

p=int(input("enter prime number"))
g=int(input("enter generator"))
n=int(input("enter how many members participating"))
arr=[]
for i in range(n):
    arr.append(int(input("enter secret key")))
    print()
#upflow
temp=[pow(g,arr[0],p)]
for i in range(n-2):
    temp.append(pow(temp[-1],arr[i+1],p))
print("key at ",n,"th user is ",pow(temp[-1],arr[-1],p))


temp.pop()
temp=[g]+temp

#downflow
 
for i in range(n-1,0,-1):

    for j in range(len(temp)):
        temp[j]=pow(temp[j],arr[i],p)
    print("key at ",i,"th user  is ",pow(temp.pop(),arr[i-1],p))