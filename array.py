from array import *


vals= array('i',[5,9,8,4,2])
#vals.reverse()

print('1:print array index by index')
for i in range(len((vals))):
    print (vals[i])
print('2:print array direct')
for e in vals:
    print(e)
print('Copy and Print a new Array')
newArr = array(vals.typecode,(a for a in vals))
for e in newArr:
    print(e)
print('Copy and Print a new Array IN POW')
newArr = array(vals.typecode,(a*a for a in vals))
for e in newArr:
    print(e)
print ('Char type')
valc= array('u',['H','A','B','I','B'])
print (valc)
for e in valc:
    print(e)
print ('New Array with while loop')

i=0
while i < len(newArr):
    print(newArr[i])
    i+=1
