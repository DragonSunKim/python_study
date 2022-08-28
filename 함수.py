def open_account():
    print("새로운 계좌가 생성되었습니다.")

# 입금
def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {} 원입니다.".format(balance + money))
    return balance + money

# 출금
def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {}원 입니다.".format(balance-money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {}원 입니다.".format(balance))
        return balance

# 저녁에 출금
def withdraw_night(balance, money):
    commission = 100 # 수수료
    return commission, balance - money - commission


balance = 0
balance = deposit(balance, 1000)
# print(balance)

# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)

commission, balance = withdraw_night(balance, 500)
print("수수료는 {}원이며, 잔액은 {}원입니다.".format(commission, balance))