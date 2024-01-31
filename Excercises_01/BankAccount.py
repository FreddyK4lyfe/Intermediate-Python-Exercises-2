    # constructor to initialize instance variable
    def init(self,account_name,starting_balance):
        self.account_name=account_name
        self.balance=starting_balance

    # method to deposit amount
    def deposit(self,amount):
        # add amount into balance
        self.balance=self.balance+amount

    # method to withdraw amount
    def withdraw(self,amount):
        # if balance is greater than or equal to amount,then withdraw amount
        if self.balance>=amount:
            # subtract amount from bal
            self.balance=self.balance-amount
        # otherwise display the message
        else:
            print("No sufficient balance to withdraw")

    # getter methods to return balance
    def get_balance(self):
        return str(self.account_name)+" has a balance of $"+str(self.balance)

    from BankAccount import BankAccount
    if __name__ == "__main__":
    # create an instance of BankAccount class
    account=BankAccount("John",1000)
    # call deposit() function
    account.deposit(400)
    # call withdraw() function
    account.withdraw(200)
    # call get_balance() function and display result
    print(account.get_balance())