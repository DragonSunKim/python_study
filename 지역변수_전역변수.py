gun = 10 # 지역 변수

def checkpoint(soldiers): # 경계근무
    global gun # 전역 공간에 있는 gun 사용
    gun -= soldiers
    print("[함수 내] 남은 총 : {}".format(gun))


def checkpoint_ret(gun, soldiers):
    gun -= soldiers
    print("[함수 내] 남은 총 : {}".format(gun))
    return gun


# print("전체 총 : {}".format(gun))
# checkpoint(2) # 2명이 경계근무 나감
# print("남은 총: {}".format(gun))


print("전체 총 : {}".format(gun))
gun = checkpoint_ret(gun, 2) # 2명이 경계근무 나감
print("남은 총: {}".format(gun))