import bank
"""
	메뉴 선택 기능 구현
"""
if __name__ == "__main__":
	lionBank = bank.BankService()

	while True:
		print("======Bank Menu=====\n1. 계좌개설\n2. 입금하기\n3. 출금하기\n4. 전체조회\n5. 계좌조회\n6. 프로그램 종료\n==================== " )

		bank_menu = input("입력 :")
		if bank_menu == str(1):
			print("======계좌개설=====")
			input("계좌번호 : ")
			input("이름 : ")
			input("예금 : ")
			print("###계좌개설을 완료하였습니다###")
			print("================")
		elif bank_menu == str(2):
			print("=====입금하기=====")
			input("입금하실 계좌번호를 입력해주세요 :")
			
			print("================")
		elif bank_menu == str(3):
			print("======출금하기======")
			input("출금하실 계좌번호를 입력해주세요 : ")
		elif bank_menu == str(4):
			print("======전체조회======")
		elif bank_menu == str(5):
			print("======개인과제======")

		elif bank_menu == str(6):
			break

