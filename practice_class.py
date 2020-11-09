class Unit:
    def __init__(self, name: str, hp: int, speed: int) -> None:
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f"{name} 유닛이 생성되었습니다.")

    def move(self, location):
        print("[지상 유닛 이동]")
        print(f"{self.name} : {location} 방향으로 이동합니다. [속도 {self.speed}]")

    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 입었습니다.")
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
        if self.hp <= 0:
            print(f"{self.name} : 파괴되었습니다.")


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


# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)
        self.location = location


# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,  "마린", 40, 1, 5)

        # 스팀팩 : 일정시간 동안 공격력 속도를 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print(f"{self.name} : 스팀팩을 사용합니다. (HP 10 감소)")
        else:
            print(f"{self.name} : 체력이 부족하여 스팀팩을 사용하지 않습니다.")


# 탱크
class Tank(AttackUnit):
    # 시즈 모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능
    seize_developed = False  # 시즈모드 개발여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if not Tank.seize_developed:
            return

        if not self.seize_mode:
            # 현재 시즈모드가 아닐때, -> 시즈모드
            print(f"{self.name} : 시즈 모드로 전환합니다.")
            self.damage *= 2
            self.seize_mode = True
        else:
            # 현재 시즈모드 일때, -> 시즈모드 해제₩
            print(f"{self.name} : 시즈모드를 해제 합니다.")
            self.damage /= 2
            self.seize_mode = False


# 레이스
class Wraith(FlyableAttcakUnit):
    def __init__(self):
        FlyableAttcakUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False  # 클로킹 모드(해제 상태)

    def cloking(self):
        if self.clocked:
            print(f"{self.name} : 클로킹 모드 해제합니다.")
            self.clocked = False
        else:
            print(f"{self.name} : 클로킹 모드 설정합니다.")
            self.clocked = True


def game_start():
    print("[알림] 새로운 게임을 시작합니다.")


def game_over():
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")


# 실제 게임 진행
game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()
w2 = Wraith()


# 유닛 일괄 관리
attack_units = [m1, m2, m3, t1, t2, w1]
