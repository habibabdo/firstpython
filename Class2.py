class Car:
    wheeles=4
    def __init__(self):
        self.mile = 10
        self.com= 'BMW'




c1=Car()

c2=Car()
Car.wheeles=11
c1.mile=8
print(c1.com , c1.mile,c1.wheeles)
print(c2.com , c2.mile,c2.wheeles)
