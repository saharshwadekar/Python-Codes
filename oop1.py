

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name,self.age)

class child(person):
    def __init__(self,name,age,section):
        self.section = section
        super().__init__(name,age)
    def display(self):
        super().display()
        print(self.section)

object = child('uno',12,'B')
object.display()