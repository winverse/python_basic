class Unit:
    def __init__(self, name: str, hp: int, speed: int) -> None:
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print(f"{self.name} : {location} 방향으로 이동합니다. [속도 {self.speed}]")

# marine1 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# wraith1 = Unit("레이스", 80, 5)
# wraith2 = Unit("레이스", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#   print(f"{wraith2.name}는 현재 클로킹 상태 입니다.")


class AttackUnit(Unit):
    def __init__(self, name: str, hp: int, speed: int,  damage: int) -> None:
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
      
    def attack(self, location: str):
        print(f"{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 {self.damage}]")
      
    def damaged(self, damage: int):
        self.hp -= damage
        print(f"{self.name} : {damage} 데미지를 입었습니다.")
        print(f"{self.name}의 현재 체력은 {self.hp}입니다.")

        if self.hp <= 0:
            print(f"{self.name} 유닛이 파괴되었습니다.")
      

# # 파이어벳 : 공격 유닛, 화염방사기
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")
#
# # 공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)

class Flyable:
    def __init__(self, flying_speed: int):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f"{name} : {location} 방향으로 날아갑니다. 속도 {self.flying_speed}")


# 공중 공격 유닛 클래스
class FlyableAttcakUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  # 지상 스피드는 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
# valkyrie = FlyableAttcakUnit('발키리', 200, 6, 5)
# valkyrie.fly(valkyrie.name, "12시")


# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저 : 공중 유닛, 체력, 공격력이 좋음
battlecruiser = FlyableAttcakUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battlecruiser.move("9시")

