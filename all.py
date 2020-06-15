
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
print(data)
for x in range(50):
    if (x + 1) % 10 == 0:
        end_char = "\n"
    else:
        end_char = "   "
    print(x,end=end_char)
html=""" <input type='tetx'> """
print(html)