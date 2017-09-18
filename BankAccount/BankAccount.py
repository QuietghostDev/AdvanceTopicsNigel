class BankAccount()

	def __init__(self, accountName, accountID, accountBalance):
		self.accountName = accountName
		self.accountID = accountID
		self.accountBalance = accountBalance
	
	def deposit(self, amount):
		self.accountBalance += amount
	
	def withdraw(self, amount):
		self.accountBalance -= amount
		
	def checkBalance(self):
		return self.accountBalance
		
newAccount = BankAccount("Nigel Hamilton", 1, 300)
print(newAccount.checkBalance())
newAccount.deposit(400)
print(newAccount.checkBalance())
newAccount.withdraw(500)
print(newAccount.checkBalance())