import fight_controller

class Player:
    def __init__(self, name, x, y, stats, level):
        self.name = name
        self.x = x
        self.y = y
        self.stats = stats
        self.inv = []
        self.level = level

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.stats["health"] > 0

    def move(self, direction):
        x_tmp = self.x
        y_tmp = self.y
        if direction == "góra":
            y_tmp -= 1
        if direction == "dół":
            y_tmp += 1
        if direction == "lewo":
            x_tmp -= 1
        if direction == "prawo":
            x_tmp += 1
        if self.level.can_move(x_tmp, y_tmp):
            self.x = x_tmp
            self.y = y_tmp
        else:
            print("Nie możesz ruszyć się w tą stronę!")

    def attack(self, target, attacktype = 'physical'):
        fight_controller.fight_controller(self, target, attacktype)

class Item:
    def __init__(self, name):
        self.name = name

