from array import *

arr=array('i',[])
n=int(input('Enter a len of Array'))

for i in range(n):
    x=int(input('enter Integer value'))
    arr.append(x)

print(arr)
for i in range(n):
    print(arr[i])

val=int(input('Enter a value to search'))
k=0
for e in arr:4
    if e == val:
        print(str(e) + ' Found in index  ' + str(k))
        break

    k+=1
