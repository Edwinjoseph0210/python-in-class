class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited: {amount}. New Balance: {self.balance}"
        return "Invalid deposit amount"
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrawn: {amount}. New Balance: {self.balance}"
        return "Invalid withdrawal amount or insufficient funds"
    
    def show_balance(self):
        return f"Current Balance: {self.balance}"

accounts = {}
while True:
    account_number = input("Enter account number (or 'q' to quit): ").strip()
    if account_number.lower() == 'q':
        break
    if account_number not in accounts:
        accounts[account_number] = BankAccount()
    account = accounts[account_number]
    
    action = input("Enter 'd' to deposit, 'w' to withdraw, 'b' to check balance, or 'q' to quit: ").strip().lower()
    if action == 'd':
        amount = int(input("Enter deposit amount: "))
        print(account.deposit(amount))
    elif action == 'w':
        amount = int(input("Enter withdrawal amount: "))
        print(account.withdraw(amount))
    elif action == 'b':
        print(account.show_balance())
    elif action == 'q':
        break
    else:
        print("Invalid option, please try again.")
