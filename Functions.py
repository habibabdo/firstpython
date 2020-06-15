def person(name,age=12):
    print(name)
    print(age)

def mathimatics(x,y):
    a=x+y
    b=x-y
    c=x*y
    d=x/y
    return a,b,c,d

def sum(*b):

    c=0
    for i in b:
        c = c + i

    print(c)

def person1(name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)


resul1,result2,result3,result4=mathimatics(10,2)
print(resul1,result2,result3,result4)

person('Habib',57)

sum(5,6,7,8,9)

person1('Habib',age='57',city='Tarshiha',mobile='0504257430')
