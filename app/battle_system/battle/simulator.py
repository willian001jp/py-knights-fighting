from typing import Dict
from ..entities.knight import Knight
from .duel import Duel


class BattleSimulator:
    def __init__(self, knights: Dict[str, Knight]) -> None:
        self.knights = knights
        self.battle_log = []

    def run_duel(self, knight1_name: str, knight2_name: str) -> None:
        """Run a duel between two knights."""
        duel = Duel(self.knights[knight1_name], self.knights[knight2_name])
        duel.fight()
        self.battle_log.append(duel.get_log())

    def run_tournament(self) -> None:
        """Run the predefined tournament duels."""
        self.run_duel("lancelot", "mordred")
        self.run_duel("arthur", "red_knight")

    def get_results(self) -> Dict[str, int]:
        """Get final HP results."""
        return {knight.name: knight.hp for knight in self.knights.values()}

    def get_full_log(self) -> str:
        """Get complete battle log."""
        return "\n\n".join(self.battle_log)
