class User:
    def __init__(self, name, initial_deposit):
        self.name = name
        self.balance = initial_deposit
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited {amount} taka")
        print(f"Username: {self.name}. Deposit {amount} taka successful. ")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdraw {amount} taka")
            print(f"Username: {self.name}. Withdraw {amount} taka successful.")
        else:
            print("Insufficient balance.")

    def check_balance(self):
        print(
            f"Username: {self.name}. Available balance: {self.balance} taka. ")

    def transfer(self, recipient, amount):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(
                f"Transferred {amount} taka to {recipient.name}")
            print(f"Transfer {amount} taka to {recipient.name} successful.")
        else:
            print("Insufficient balance.")

    def check_transaction_history(self):
        print(f"\nTransaction History of {self.name} :")
        for transaction in self.transaction_history:
            print(transaction)

    def take_loan(self, bank):
        loan_amount = 2 * self.balance
        self.balance += loan_amount
        bank.total_loan_amount += loan_amount
        self.transaction_history.append(
            f"Username: {self.name}. Took a loan of {loan_amount} taka.")
        print(
            f"Username: {self.name}. Loan of {loan_amount} taka taken successfully.")
