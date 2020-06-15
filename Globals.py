
a=15

def something():
     a=10
     print (a)
     x=globals()['a']
     print (x)
     globals()['a']=100

print('LOCAL:')
something()
print('GLOBAL:')
print(a)

def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

lst=[1,22,3,44,5,6,44,33,77,88,6,90]
E,O=count(lst)
print('EVEN=' ,E)
print('ODD=',O)
print('EVEN {} and ODD {}'.format(E,O))
