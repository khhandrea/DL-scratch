class Bank:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        print(f'welcome, {name}!')

    def deposit(self, amount):
        self.balance += amount
        print('deposited successfully')

    def withdraw(self, amount):
        if amount > self.balance:
            print('too many money!')
        else:
            self.balance -= amount
            print('withdrawed successfully')
    
    def check(self):
        print(f"{self.name}'s balance is {self.balance}")

if __name__ == '__main__':
    m = Bank("Kim")
    m.withdraw(5000)
    m.deposit(4000)
    m.withdraw(2000)
    m.check()