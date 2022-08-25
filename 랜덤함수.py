from random import *

# random() : 0.0 ~ 1.0 임의의 값 생성
print(random())

print(random() * 10) 

# 0 ~ 10 미만의 임의의 정수
print(int(random() * 10))

# 1 ~ 46 미만의 임의의 값 생성
print(randrange(1, 46))

# 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45))