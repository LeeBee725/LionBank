import bank
import bank.error as err
"""
	메뉴 선택 기능 구현
"""

def select_account(inputMessage):
	global lionBank
	accountId = input(inputMessage)
	err.raise_error_if_invalid_id(accountId)
	account = lionBank.getAccount(accountId)
	print(f"계좌이름 : {account.name}")
	print(f"계좌잔고 : {account.balance}원")
	return account

def create_account_by_user():
	global lionBank
	id = input("계좌번호 : ")
	err.raise_error_if_invalid_id(id)
	if lionBank.accounts.get(id, None) != None:
		raise err.InvalidIdException("이미 존재하는 계좌입니다.")
	name = input("이름 : ")
	err.raise_error_if_invalid_name(name)
	balance = input("예금 : ")
	err.raise_error_if_invalid_cash(balance)
	return bank.Account(id, name, int(balance))

if __name__ == "__main__":
	lionBank = bank.BankService()

	while True:
		try:
			print("======Bank Menu=====\n1. 계좌개설\n2. 입금하기\n3. 출금하기\n4. 전체조회\n5. 계좌조회\n6. 프로그램 종료\n==================== " )

			bank_menu = input("입력 :")
			err.raise_error_if_invalid_userInput(bank_menu)
			if bank_menu == str(1):
				print("======계좌개설=====")
				account = create_account_by_user()
				lionBank.add_account(account)
				print("###계좌개설을 완료하였습니다###")
				print("================")
			elif bank_menu == str(2):
				print("=====입금하기=====")
				account = select_account("입금하실 계좌번호를 입력해주세요 :")
				cost = input("입금하실 금액을 입력해주세요 : ")
				err.raise_error_if_invalid_cash(cost)
				lionBank.deposit_account(account, int(cost))
				print(f"\n## 계좌잔고 : {account.balance:11d} 원 ##")
				print("## 입금이 완료되었습니다 ##")
				print("================")
			elif bank_menu == str(3):
				print("======출금하기======")
				account = select_account("출금하실 계좌번호를 입력해주세요 :")
				cost = input("출금하실 금액을 입력해주세요 : ")
				err.raise_error_if_invalid_cash(cost)
				balance = lionBank.withdraw_account(account, int(cost))
				if balance < 0:
					print("\n잔액부족")
					continue
				print(f"\n## 계좌잔고 : {account.balance:11d} 원 ##")
				print("## 출금이 완료되었습니다 ##")
				print("================")
			elif bank_menu == str(4):
				print("======전체조회======")
				accounts = lionBank.get_total_accounts().values()
				if len(accounts) == 0:
					print("등록된 계좌가 없습니다.")
					continue
				for account in accounts:
					print(account)
				print("====================")
			elif bank_menu == str(5):
				print("======개인과제======")

			elif bank_menu == str(6):
				print("##프로그램을 종료합니다##")
				break
		except KeyError as k:
			print("\n===존재하지 않는 계좌입니다.===")
		except Exception as e:
			print(e)

