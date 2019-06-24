import fight_controller

class Enemy:
    def __init__(self, name, stats):
        self.name = name
        self. stats = stats

    def __repr__(self):
        return self.name

    def attack(self, target):
        fight_controller.fight_controller(self, target, "physical")

    def is_alive(self):
        return self.stats["health"] > 0
