class Computer:
    def __init__(self):
        self.name='Habib'
        self.age=57

    def update(self):
        self.age=17

    def compair(self,other):
        if self.age==other.age:
            return True
        else:
            return False





c1=Computer()
c1.name='Abdo'
c2=Computer()
c2.update()
c1.update()
print(c1.name)
print(c2.name)

if c1.compair(c2):
    print ('The Same Age')
else:
    print('Not The Same')
