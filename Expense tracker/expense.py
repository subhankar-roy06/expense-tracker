class Expense:
    def __init__(self, name, catagory ,amount)->None:
        self.name = name
        self.catagory = catagory
        self.amount = amount
    def __repr__(self):
        return f"<Expense: {self.name}, {self.catagory} ,{self.amount}>"