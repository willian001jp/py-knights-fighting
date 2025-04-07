from battle_system.config.knights import KNIGHTS_CONFIG
from battle_system.entities.knight import Knight
from battle_system.battle.simulator import BattleSimulator


def initialize_knights() -> dict[str, Knight]:
    """Create knight instances from configuration"""
    return {name: Knight(**data) for name, data in KNIGHTS_CONFIG.items()}


def run_battle() -> dict[str, int]:
    """Run the battle simulation and return results"""
    knights = initialize_knights()
    simulator = BattleSimulator(knights)
    simulator.run_tournament()

    print("\n=== Battle Log ===")
    print(simulator.get_full_log())

    print("\n=== Final Results ===")
    for knight in knights.values():
        print(knight)

    return simulator.get_results()


if __name__ == "__main__":
    results = run_battle()
    print("\nResults:", results)
