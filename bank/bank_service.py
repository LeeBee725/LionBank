# from .account import Account

class BankService:
	def __init__(self):
		self.accounts = {}

	def add_account(self, account):
		self.accounts[account.id] = account

	def deposit_account(self, account, cost):
		account.deposit(cost)

	def withdraw_account(self, account, cost):
		account.withdraw(cost)
	
	def get_total_accounts(self):
		return self.accounts

	def getAccount(self, accountId):
		return self.accounts[accountId]

	
