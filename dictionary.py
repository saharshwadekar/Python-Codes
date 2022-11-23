from psutil import swap_memory


class stdId:
    def __init__(self,*a):
        self.Name = a[0]
        self.Id = a[1]
        self.Dob = a[2]
        self.version = a[3]
    def species(self):
        pass
    def printing(self):
        print(self.Dob,self.Id,self.Name,self.version)

# object
person1 = stdId("Saharsh",23,2002,11.5)
person1.printing()
