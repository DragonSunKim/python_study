class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")


class AttackUnit(Unit):
    def __init__(self):
        # Unit.__init__(self)
        super().__init__() # 부모클래스를 호출한다. self를 적지 않는다. 

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__() # 두 개이상의 클래스를 상속받을때 맨 앞의 클래스가 호출 받는다.
        Unit.__init__(self)
        Flyable.__init__(self)
    

# AttackUnit()

FlyableUnit()