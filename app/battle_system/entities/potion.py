from dataclasses import dataclass
from ..entities.knight import Knight


@dataclass
class PotionEffect:
    power: int = 0
    hp: int = 0
    protection: int = 0


@dataclass
class Potion:
    name: str
    effect: PotionEffect

    def apply(self, target: Knight) -> None:
        """Apply potion effects to target knight."""
        target.power += self.effect.power
        target.hp += self.effect.hp
        target.protection += self.effect.protection
