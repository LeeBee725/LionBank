# from .account import Account

class BankService:
	def __init__(self):
		self.accounts = {}

	def add_account(self, account):
		self.accounts[account.id] = account

	def deposit_account(self, account, cost):
		account.deposit(cost)
		return account.balance + cost

	def withdraw_account(self, account, cost):
		balance = account.balance
		if balance >= cost:
			account.withdraw(cost)
		return balance - cost
	
	def get_total_accounts(self):
		return self.accounts

	def getAccount(self, accountId):
		return self.accounts[accountId]

	def remove_account(self, account):
		del self.accounts[account.id]
