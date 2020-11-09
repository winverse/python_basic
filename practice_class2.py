class Unit:
    def __init__(self):
        print("Unit 생성자")


class Flyable:
    def __init__(self):
        print("Flyable 생성자")


class FlyableUnit(Flyable, Unit):
    def __init__(self):
        # super().__init__() 다중 상속을 하게될때 super를 사용하게 되면 맨 처음 오는 class만 실행한다는 문제점이 존재한다.
        Flyable.__init__(self)
        Unit.__init__(self)


# 드랍쉽
dropship = FlyableUnit()