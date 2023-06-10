from Admin import Admin

def main():

    bank_admin = Admin()

# Creating customer accounts
    bank_admin.create_account("Rahat", "12345",  3000)
    bank_admin.create_account("Zayed", "54321", 8000)

# Depositing and withdrawing amount
    customer_1 = bank_admin.customers[0]
    customer_1.deposit(4000,bank_admin)
    customer_1.withdraw(2000,bank_admin)

# Checking available balance
    customer_1.check_balance()

# Transferring amount
    customer_2 = bank_admin.customers[1]
    customer_1.transfer(customer_2, 1500)

# Taking a loan
    if bank_admin.loan_enabled:
        customer_1.take_loan(bank_admin)
    else:
        print("Loan  is currently disabled.")

# Checking transaction history
    customer_1.check_transaction_history()


# Admin operations
    bank_admin.check_total_balance()
    bank_admin.check_total_loan_amount()
    bank_admin.disable_loan()



# Checking if the bank is bankrupt
    if bank_admin.is_bankrupt():
        print("Bank is bankrupt.")
    else:
        print("Bank is not bankrupt.")


if __name__ == '__main__':
    main()
