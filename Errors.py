a=5
b=0
try:
    print('Resource opened')
    print(a/b)
    k=int(input('Enter A Number'))
    print(k)
except ZeroDivisionError as e:
    print('You Cannot devide by ZERO',e)
except ValueError as e:
    print('Invalid input')
except Exception as e:
    print('Some thing wrong ')
finally :
    print('resources Closed')
print('Bye')



