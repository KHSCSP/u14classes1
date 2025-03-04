class Student:
    
    # this initializer receives a string and an integer
    def __init__(self, nameP, ageP):
        print("...creating a student object...")
        self.name = nameP
        self.age = ageP
      
    def __str__(self):
        #print("...the __str__ function was called...")
        return self.name + " is " + str(self.age) + " years old"