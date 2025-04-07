from dataclasses import dataclass


@dataclass
class ArmorPiece:
    part: str
    protection: int


@dataclass
class Weapon:
    name: str
    power: int

    def __str__(self) -> str:
        return f"{self.name} (Power: {self.power})"
