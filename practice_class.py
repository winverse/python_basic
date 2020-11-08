class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{name} 유닛이 생성 었습니다.")
        print(f"체력 {hp}, 공격력 {damage}")


# marine1 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# wraith1 = Unit("레이스", 80, 5)
# wraith2 = Unit("레이스", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#   print(f"{wraith2.name}는 현재 클로킹 상태 입니다.")

class AttackUnit:
    def __init__(self, name: str, hp: int, damage: int):
        self.name = name
        self.hp = hp
        self.damage = damage
      
    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 {self.damage}]")
      
    def damaged(self, damage):
        self.hp -= damage
        print(f"{self.name} : {damage} 데미지를 입었습니다.")
        print(f"{self.name}의 현재 체력은 {self.hp}입니다.")

        if self.hp <= 0:
            print(f"{self.name} 유닛이 파괴되었습니다.")
      

# 파이어벳
firebat1 = AttackUnit("파이어뱃", 50, 16)
