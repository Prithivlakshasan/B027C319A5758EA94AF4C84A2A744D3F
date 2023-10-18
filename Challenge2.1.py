# 2.1 Implement a class called bankaccount that represents a bankaccount.the class should have private attributes for account number,account holder name and bank balance.include methods to deposit money,withdraw money and display the account balance.ensure that  the account balance cannot be accessed directly outside the class.write a program to create an instance of the bank account class and test the deposit and withdrawal functionality


class bankaccount:

    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print("Deposited ₹{}. New balance: ₹{}".format(amount, self.__account_balance))
        else:  
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            print("Withdraw ₹{}. New balance: ₹{}".format(amount, self.__account_balance))
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def display_balance(self):
        print("Account balance for {} (Account #{}): ₹{}".format(
            self.__account_holder_name, self.__account_number, self.__account_balance))


# create an instance of the bankaccount class
account = bankaccount(account_number="1234567890",
                      account_holder_name="karthikeyan",
                      initial_balance=100000.0)

# test deposit and withdrawal functionality
account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.withdraw(200000.0)
account.display_balance()
