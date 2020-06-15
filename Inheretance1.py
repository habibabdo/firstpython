class A:
    def __init__(self):
        print('In A INIT')

    def feature1(self):
        print('Feature 1 Working')


    def feature2(self):
        print('Feature 2 Working')

class B:

    def __init__(self):

        print('IN B INIT')

    def feature3(self):
        print('Feature 3 Working')


    def feature4(self):
        print('Feature 4 Working')

class C(A,B):
    def __init__(self):
        super().__init__()
        print('In  C INIT')
        
    def feat(self):
        super().feature2()


b1=C()
b1.feat()
