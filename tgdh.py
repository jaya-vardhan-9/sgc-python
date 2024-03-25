import math

n=4
arr=[9,10,11,12]
p,g=11,6


for k in range(math.ceil(math.log2(n))):
    new_arr = []
    for i in range(0,len(arr),2):
        if i+1==len(arr):
            new_arr.append( pow(pow(g,arr[i],p) ,arr[i+1],p) )
        else:
            new_arr.append(arr[i]+arr[i+1])
    print(new_arr)
    arr=new_arr[:]