from ..entities.equipment import ArmorPiece, Weapon
from ..entities.potion import Potion, PotionEffect

KNIGHTS_CONFIG = {
    "lancelot": {
        "name": "Lancelot",
        "base_power": 35,
        "base_hp": 100,
        "weapon": Weapon("Metal Sword", 50),
        "armor": [],
        "potion": None,
    },
    "arthur": {
        "name": "Arthur",
        "base_power": 45,
        "base_hp": 75,
        "weapon": Weapon("Two-handed Sword", 55),
        "armor": [
            ArmorPiece("helmet", 15),
            ArmorPiece("breastplate", 20),
            ArmorPiece("boots", 10),
        ],
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "base_power": 30,
        "base_hp": 90,
        "weapon": Weapon("Poisoned Sword", 60),
        "armor": [
            ArmorPiece("breastplate", 15),
            ArmorPiece("boots", 10),
        ],
        "potion": Potion("Berserk", PotionEffect(power=15, hp=-5, protection=10)),
    },
    "red_knight": {
        "name": "Red Knight",
        "base_power": 40,
        "base_hp": 70,
        "weapon": Weapon("Sword", 45),
        "armor": [
            ArmorPiece("breastplate", 25),
        ],
        "potion": Potion("Blessing", PotionEffect(hp=10, power=5)),
    }
}
