from .account import Account

class BankService:
	def __init__(self):
		self.accounts = {}

	def add_account(self, account):
		self.accounts[account.id] = account

	def deposit_account(self, account, cost):
		account.deposit(cost)  #account?
		return account.balance + cost

	def withdraw_account(self, account, cost):
		balance = account.balance
		if balance >= cost:
			account.withdraw(cost)
		return balance - cost
	
	def get_total_accounts(self):
		return self.accounts

	def send_account(self, account_from, account_to, cost):
		account_from.deposit(cost)
		account_to.withdraw(cost)
		pass

	def getAccount(self, accountId):
		find = self.accounts[accountId]
		return find

	
