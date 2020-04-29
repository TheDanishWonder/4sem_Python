

class Person(Exception):
    
    def __init__(self, name):
        self.name = name


    def onlyLet(self):
        for char in self.name:
            if(str.isalpha == True) in self.name:
                print(self.name)
            else:
                raise Person('The name may only be letters')
p1 = Person('Jack')
p2 = Person('Jack.')          

print(p2)       
