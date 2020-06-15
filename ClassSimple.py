class person:

    def __init__(self,fname,lname,city,age):
        self.fname=fname
        self.lname=lname
        self.city=city
        self.age=age

    def show(abc):
        print(abc.fname,p1.lname,p1.city,abc.age,)

class city:
    def __init__(self,city):
        self.city=city


p1=person('Habib','Abdo','Tarshiha',57)

p1.show()
p1.age=18
del  (p1.lname)
p1.fname=input('Enter First Name')

p1.lname=input('Enter Last Name')
p1.city='Fassota'
p1.show()
c1=city('karmel')
print(c1.city)



