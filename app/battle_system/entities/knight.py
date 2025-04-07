from dataclasses import dataclass, field
from typing import List, Optional
from .equipment import ArmorPiece, Weapon
from .potion import Potion


@dataclass
class Knight:
    name: str
    base_power: int
    base_hp: int
    weapon: Weapon
    armor: List[ArmorPiece] = field(default_factory=list)
    potion: Optional[Potion] = None

    def __post_init__(self):
        self.power = self.base_power + self.weapon.power
        self.hp = self.base_hp
        self.protection = sum(piece.protection for piece in self.armor)

        if self.potion:
            self.potion.apply(self)

    def take_damage(self, damage: int):
        """Apply damage to knight, ensuring HP doesn't go below 0"""
        self.hp = max(0, self.hp - damage)

    def attack(self, opponent: 'Knight'):
        """Attack another knight"""
        damage = max(0, self.power - opponent.protection)
        opponent.take_damage(damage)
        return damage

    @property
    def is_alive(self) -> bool:
        """Check if knight is still alive"""
        return self.hp > 0

    def __str__(self):
        status = "Alive" if self.is_alive else "Defeated"
        return (f"{self.name}: {status} | "
                f"HP: {self.hp} | "
                f"Power: {self.power} | "
                f"Protection: {self.protection}")
