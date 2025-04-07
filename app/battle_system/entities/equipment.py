from dataclasses import dataclass
from typing import Optional

@dataclass
class ArmorPiece:
    part: str
    protection: int

@dataclass
class Weapon:
    name: str
    power: int

    def __str__(self):
        return f"{self.name} (Power: {self.power})"
