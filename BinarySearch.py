pos =-1


def search(list,n):
    l=0
    u=len(list)
    print(u)
    while l <= u:
        mid=(l+u)//2

        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid] < n:
                l = mid
            else:
                u = mid
    return False



list=[4,7,8,12,45,99,102]
n=8
if search(list,n):
    print ('Found at ' ,pos+1)
else:
    print('Not Found')

