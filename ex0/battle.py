from ex0 import FlameFactory, AquaFactory, CreatureFactory, Creature


def verify_factory(factory: CreatureFactory) -> None:
    print("\nTesting factory")
    base: Creature = factory.create_base()
    evolved: Creature = factory.create_evolved()

    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def battle(f1: CreatureFactory, f2: CreatureFactory) -> None:
    print("\nTesting battle")
    c1: Creature = f1.create_base()
    c2: Creature = f2.create_base()

    print(c1.describe())
    print("vs.")
    print(c2.describe())
    print("fight!")
    print(c1.attack())
    print(c2.attack())


if __name__ == "__main__":
    flame_f: FlameFactory = FlameFactory()
    aqua_f: AquaFactory = AquaFactory()

    verify_factory(flame_f)
    verify_factory(aqua_f)
    battle(flame_f, aqua_f)
