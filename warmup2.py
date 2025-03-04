# we want to store customer information for a bank
# name, account number, money
# let's explore 3 options: lists, dictionaries, class

# --- option 1, OMG so bad, parallel lists
names = []
nums = []
monies = []
# create one or two customers

# how could we add money to their account?
# how could we print each customer in a neat way?




# --- option 2, a list of dictionaries, not too bad, but...
customers = []
# create one or two customers

# how could we add money to their account?
# how could we print each customer in a neat way?






# --- option 3, a class, welcome to the future
class Customer:
    def __init__(self, nameP, numP, moneyP):
        self.name = nameP
        self.num = numP
        self.money = moneyP
    
    def add_money(self, amt):
        self.money += amt


# create a few customer objects



