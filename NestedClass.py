
class student:

    school='Tarshiha'

    def __init__(self,name,rolino):
        self.name=name
        self.rolino=rolino
        self.lap=self.Laptop()

    def show(self):
        print(self.name,self.rolino)
        self.lap.show()

    class Laptop:
        def __init__(self):
          self.brand='HP'
          self.cpu='15'
          self.ram=8

        def show(self):
            print(self.brand ,self.cpu,self.ram)




s1=student('Habib',2)
s2=student('Abdo',3)

s1.show()
s2.show()
lap1=s1.lap
lap2=s2.lap
print(id(lap1))
print(id(lap2))
