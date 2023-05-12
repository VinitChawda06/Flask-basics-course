####################################################
####################################################
# Object Oriented Programming Challenge - Solution
####################################################
####################################################
#
# For this challenge, create a bank account class that has two attributes:
#
# * owner
# * balance
#
# and two methods:
#
# * deposit
# * withdraw
#
# As an added requirement, withdrawals may not exceed the available balance.
#
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
class Account:
    
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def __repr__(self):
        return f"Owner:{self.owner} , Balance:{self.balance}"

    def deposit(self,d_amt):
        self.balance += d_amt
        return f"Balance after deposit:{self.balance}"

    def withdraw(self,w_amt):
        if self.balance >= w_amt:
            self.balance -= w_amt
            return f"Balance after withdrawal:{self.balance}"
        else:
            return "Withrdrawal amount is greater than your balance"

# 1. Instantiate the class
acct1 = Account('Jose',100)


# 2. Print the object
print(acct1)




# 3. Show the account owner attribute
print(acct1.owner)




# 4. Show the account balance attribute
print(acct1.balance)




# 5. Make a series of deposits and withdrawals
print(acct1.deposit(50))




print(acct1.withdraw(20))




# 6. Make a withdrawal that exceeds the available balance
print(acct1.withdraw(500))

# ## Good job!
