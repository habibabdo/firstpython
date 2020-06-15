
class student:

    school='Tarshiha'

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avf(self):
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):
        return self.m1

    def set_m1(self,value):
        self.m1=value

    @classmethod
    def getschool(cls):
        return  cls.school
    @staticmethod
    def info():
        print('This is Tarshiha School')



s1=student(34,67,32)
s2=student(89,32,12)

print(s1.avf())
print(s2.avf())
print(student.getschool())
student.info()
