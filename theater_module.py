# 모듈.py에서 이용
# 일반 가격
def price(people):
    print("{}명 가격은 {}원 입니다.".format(people, people*10000))

# 조조 할인 가격
def price_morning(people):
    print("{}명 가격은 {}원 입니다.".format(people, people*6000))

# 군인 할인 가격
def price_soldier(people):
    print("{}명 가격은 {}원 입니다.".format(people, people*4000))