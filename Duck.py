
class python:
    def execute(self):
        print ('compiling')
        print('running')


class MyEditor:

    def execute(self):
        print('Spell Check')
        print('Covention Check')
        print ('compiling')
        print('running')

class Laptop:
    def code(self,ide):
        ide.execute()
        


ide=MyEditor()
lap1=Laptop()
lap1.code(ide)
print('\nchange ide from myeditor class to python class:\n')
ide=python()
lap1=Laptop()
lap1.code(ide)
