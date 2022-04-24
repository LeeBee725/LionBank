class Account:
	def __init__(self, id, name, balance):
		self.id = id
		self.name = name
		self.balance = balance
	
	def deposit(self, money):
		self.balance += money  #balance

	def withdraw(self, money):
		self.balance -= money

	# 객체 하나가 화면에 출력되는 형식을 지정
	def __str__(self):
		return "계좌번호 : " + str(self.id) + " / 이름 : " + str(self.name) + " / 잔액 : " +str(self.balance)

# Testing code
if __name__ == "__main__":
	lion = Account(12345, "sungjin", 30000)
	lion.deposit(10000)
	print(lion)


