class Unit:
    def __init__(self, name, hp, damage):
        self.name = name # 멤버 변수
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {}, 공격력 {}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

wraith1 = Unit("레이스", 80, 5)
print("유닛 이름: {}, 공격력: {}".format(wraith1.name, wraith1.damage))


wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{} 는 현재 클로킹 상태입니다.".format(wraith2.name))