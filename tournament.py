from ex0.creatures import (
    FlameFactory, AquaFactory, CreatureFactory, Creature
)

from ex1.capacities import (
    HealingCreatureFactory,
    TransformCreatureFactory
)

from ex2.strategies import (
    NormalStrategy, AggressiveStrategy,
    DefensiveStrategy, BattleStrategy,
)

from ex2.exceptions import (
    InvalidStrategyError
)


def tournament_battle(
    opponents: list[tuple[CreatureFactory, BattleStrategy]]
) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    try:
        for i in range(len(opponents)):
            for j in range(i + 1, len(opponents)):
                f1, s1 = opponents[i]
                f2, s2 = opponents[j]
                c1: Creature = f1.create_base()
                c2: Creature = f2.create_base()

                print("\n* Battle *")
                print(c1.describe())
                print("vs.")
                print(c2.describe())
                print("now fight!")

                s1.act(c1)
                s2.act(c2)
    except InvalidStrategyError as e:
        print(f"Battle error, aborting tournament: {e}")


if __name__ == "__main__":
    flame_f = FlameFactory()
    aqua_f = AquaFactory()
    heal_f = HealingCreatureFactory()
    trans_f = TransformCreatureFactory()

    norm_s = NormalStrategy()
    aggr_s = AggressiveStrategy()
    def_s = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    tournament_battle([(flame_f, norm_s), (heal_f, def_s)])

    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    tournament_battle([(flame_f, aggr_s), (heal_f, def_s)])

    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    tournament_battle([(aqua_f, norm_s), (heal_f, def_s), (trans_f, aggr_s)])
