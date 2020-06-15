from typing import Union

print('Habib elias Abdo')

num = [11,12,23,34,45,67,78]
print(num)
sm = sum(num)
print(sm)
av = range(sm)
print(sm)
num.sort()
print(num)
tup = (12,43,45,56,78,89)
print(tup[1])
print(tup[0])

s = {12,23,23,45,43,45,67}

print(s)
data = {1: 'Habib',2: 'Elias',3: 'Abdo',4: 'Madlen'}
print(data)
print(data[4])
print(data.get(2))
print(data.get(10,'Not Found'))
keys = ['aaa','bbb','ccc','ddd','fff']
values = ['AAA','BBB','CCC','DDD']
data = dict(zip(keys,values))
print(data)
print(data['aaa'])

del data['aaa']
print(data)
data['sss'] = 'SSSSSS'
# print(data)
for x in range(100):
    if (x + 1) % 10 == 1:
        end_char = "\n"
    else:
        end_char = "   "
    print(x,end=end_char)
html = """ <input type='tetx'> """
print(html)
prog = {'aaa': 'AAA','bbb': 'BBB','CCC': ['aaa','bbb','ccc','ddd'],'JAVA': {'qqq': 'QQQ','rrr': 'RRR','ttt': 'TTT'}}
print(prog)
# Addresses
num = 5
c = "ID OF num =" + str( id(num))
print(c)
s={1,4,2,3,6,7,8,9,0,9}
print(s)
print(type(c))
print('list 1 to 10 :')
print(list (range(10)))
print('print all even numbers 1 to 10 :')
print(list (range(2,10,2)))
print('Dictionary')
d={'Habib':'PC','Nedal':'dentest','Elias':'enginer','Madlen':'Teacher'}
print(d)
print('Keys')
print(d.keys())
print('Values')
print(d.values())
print(d.get('Habib'))
print(d['Habib'])
print('Operators')
a=4
b=7
print(a<b )
print(a<8 and b>8 )
print('Binary')
print(bin(25))
print('Octan')
print(oct(25))
print('Hex')
print(hex(25))
print('Swap')
a=10
b=5
a,b=b,a
print(  a ,  b)

print ('BITWISE: & | ^')
print('12 AND 13:')
print(12&13)

print(bin(12))
print(bin(13))
print(bin(12))
print('12 OR 13:')
print (12| 13)
print(bin(12))
print(bin(13))
print(bin(13))

print ('In XOR 2 defferent numbers are equal to 1')
print (12^13)
print(25^30)
print(bin(25))
print (bin(30))
print(bin(7))
print('LEFT and RIGHT SHIFT:')
print('10 LEFT SHIFT 2 =  ' + str((10<<2)))
print('10 Right  SHIFT 2 = ' + str((10>>2)))
print('Binary Of 10 is : ' + bin(10))
print('Binary Of 2 is : ' + bin(2))
print('Binary Of 40 is : ' + bin(40))
