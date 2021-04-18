class Budget:

    def __init__(self, focus, amount):
        self.category = focus
        self.budget = amount

    def deposit(self, amount):
        self.budget += amount
    
    def withdraw(self, amount):
        if self.budget < amount:
            exit("You cannot afford this lifestyle!!!")
        self.budget -= amount

    def transfer(self, focus, amount):
        if self.budget < amount:
            exit(f"You really do not have enough to transfer to {focus} category!")
        focus.budget += amount
        self.budget -= amount
    
    def checkBalance(self):
        print(f"You have only {self.budget} left to spend on {self.category}!")

