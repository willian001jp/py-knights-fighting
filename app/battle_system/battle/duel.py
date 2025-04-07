from typing import Tuple
from ..entities.knight import Knight


class Duel:
    def __init__(self, knight1: Knight, knight2: Knight) -> None:
        self.knight1 = knight1
        self.knight2 = knight2
        self.log = []

    def fight(self) -> Tuple[int, int]:
        """Execute duel between two knights."""
        damage1 = self.knight1.attack(self.knight2)
        damage2 = self.knight2.attack(self.knight1)

        self.log.append(
            f"{self.knight1.name} hits "
            f"{self.knight2.name} for {damage1} damage"
        )
        self.log.append(
            f"{self.knight2.name} hits "
            f"{self.knight1.name} for {damage2} damage"
        )

        return self.knight1.hp, self.knight2.hp

    def get_log(self) -> str:
        """Get formatted battle log."""
        return "\n".join(self.log)
