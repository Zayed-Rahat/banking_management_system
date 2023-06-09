from Users import User

class Admin:
    def __init__(self):
        self.customers = []
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_enabled = True

    def create_account(self, name, password, initial_deposit):
        new_customer = User(name, password, initial_deposit)
        self.customers.append(new_customer)
        self.total_balance += initial_deposit
        print(f"Account created for {name}. Initial amount: {initial_deposit}")

    def check_total_balance(self):
        self.total = self.total_balance - self.total_loan_amount
        print(f"\nTotal available balance in the bank: {self.total}")

    def check_total_loan_amount(self):
        print(f"Total loan amount in the bank: {self.total_loan_amount}")

    def enable_loan(self):
        self.loan_enabled = True
        print("Loan enabled.")

    def disable_loan(self):
        self.loan_enabled = False
        print("Loan disabled.")

    def is_bankrupt(self):
        return self.total_balance < 0
