# try:
#     print("나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2= int(input("두 번째 숫자를 입력하세요 : "))

#     print("{} / {} = {}".format(num1, num2, num1/num2))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")

# except ZeroDivisionError as err:
#     print(err)

class BigNumberError(Exception): # 사용자 정의 예외처리
    def __init__(self, msg):
        self.msg = msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))

    if num1 >= 10 or num2 >= 10:
        
        # 오류 발생
        raise BigNumberError("입력값 : {}, {}".format(num1, num2))

    print("{} / {} = {}".format(num1, num2, num1 / num2))
except ValueError:
    print("잘못된 값 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력해주세요.")
    print(err)

finally:
    print("이용해 주셔서 감사합니다.")