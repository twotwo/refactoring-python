from dataclasses import dataclass


@dataclass
class Soldier:
    health: int = 0
    damage: int = 0
    weaponStatus: int = 0


@dataclass
class Weapon:
    damage: int = 0
    weaponStatus: int = 0


@dataclass
class SoldierAfter:
    health: int = 0
    weapon: Weapon = Weapon()


if __name__ == "__main__":

    print("SoldierAfter", SoldierAfter(health=100, weapon=Weapon(damage=10, weaponStatus=10)))
