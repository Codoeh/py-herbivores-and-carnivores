class Animal:
    """
    Class animal contains animals name,
    also health and hidden with default parameters.
    It's store alive animals in alive list of dicts,
    if animal's health > 0.
    """
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden

        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f'kotName: {self.name}, Health: {self.health}, '
                f'Hidden: {self.hidden}pies').replace(
            "kot", "{").replace("pies", "}")


class Herbivore(Animal):
    """
    Herbivore class inherit from Animal. Also has
    a method hide, which changes the hidden value,
    to the opposite.
    """
    def hide(self) -> None:
        if self.hidden is False:
            self.hidden = True
        elif self.hidden is True:
            self.hidden = False


class Carnivore(Animal):
    """
    Carnivore class inherit from Animal. Also has
    a method bite, which substract 50 health from
    Herbivore, if health >= 0, else it's removing
    Herbivore from Animal.alive list.
    """
    def bite(self, other: Animal) -> None:
        if isinstance(other, Carnivore):
            print(f"{self.name} cannot bite other carnivore.")
        elif other.hidden is True:
            print(f"{self.name} cannot bite hidden {other.name}")
        else:
            if other.health > 0:
                other.health -= 50
                if other.health <= 0:
                    print(f"{other.name} is dead.")
                    Animal.alive.remove(other)
                else:
                    print("Bited")
