class Animal:
    
    # this initializer does not receive any parameters
    def __init__(self):
        self.name = input("what type of animal is this? ")
        self.legs = int(input("how many legs does it have (number)? "))
        temp = input("does it have fur? ").lower()
        if temp == 'y' or temp == 'yes':
            self.fur = True
        else:
            self.fur = False
    
