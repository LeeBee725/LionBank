ID_SIZE = 13

VALID_INPUT_NUMBER = "123456"

def is_invalid_id_size(accountId):
	return len(accountId) != ID_SIZE

def is_invalid_nums(string):
	return not string.isdecimal()

def raise_error_if_invalid_id(accountId):
	if is_invalid_id_size(accountId) or is_invalid_nums(accountId):
		raise InvalidIdException()

def raise_error_if_invalid_cash(cash):
	if is_invalid_nums(cash):
		raise InvalidCashException()

def raise_error_if_invalid_userInput(userInput):
	if len(userInput) != 1 or VALID_INPUT_NUMBER.find(userInput) == -1:
		raise InvalidUserInputException()

class InvalidIdException(Exception):
	def __init__(self):
		super().__init__("계좌번호 입력이 올바르지 않습니다.")

class InvalidCashException(Exception):
	def __init__(self):
		super().__init__("금액 입력이 올바르지 않습니다.")

class InvalidUserInputException(Exception):
	def __init__(self):
		super().__init__("===잘못된 입력입니다.===")