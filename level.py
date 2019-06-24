from minigames import *
import minigames
from mob import *
import functools


class Level:
    def __init__(self, rooms, number):
        self.rooms = rooms
        self.number = number
        # self.games = games

    def can_move(self, x, y):
        if x in [0, 1] and y in [0, 1, 2]:
            return True
        return False

    def print_map(self):
        if self.number == 0:
            print(""" ___________________
|          |        |
|Magazyn I |        |
|                   |
|__  ______|        |
|       |   Magazyn |
|Toaleta|______II___|
|                   |
|       | Zaplecze  |
|___  __|______  ___|
|          |        |
| Recepcja   Biuro  |
|          |        |
|          |        |
|__________|________|""")
        if self.number == 1:
            print("mapa 2")

    def is_cleared(self):
        rooms_with_quest = []
        for row in self.rooms:
            for room in row:
                if room.quest is not None:
                    rooms_with_quest.append(room)
        is_cleared = True
        for room in rooms_with_quest:
            is_cleared = is_cleared and room.quest.completed
        return is_cleared


class Room:
    def __init__(self, name, description, x, y, items, quest, enemy):
        self.name = name
        #self.description = description
        self.x = x
        self.y = y
        self.items = items
        self.quest = quest
        self.enemy = enemy

    def __str__(self):
        return self.name #+ ' - ' + self.description.lower()

    def __repr__(self):
        return self.name

    #def enter(self):
     #   print(self.description)


def level_gen(number_of_levels):
    levels = []
    lvl_1 = open("lvl_1.txt", 'r', encoding="utf8")
    lvl_2 = open("lvl_2.txt", 'r', encoding="utf8")
    room_3 = None
    for n in range(number_of_levels):
        if n == 0:
            rooms = room_gen(lvl_1, n + 1)
            levels.append(Level(rooms, n + 1))
        if n == 1:
            rooms = room_gen(lvl_2, n + 1)
            levels.append(Level(rooms, n + 1))
    lvl_1.close()
    lvl_2.close()
    return levels


def room_gen(rooms_d, lvl_no):
    rooms_out = []
    if lvl_no == 1:
        for i in range(3):
            rooms_in = []
            for j in range(2):
                rooms_desc = (rooms_d.readline().rstrip(), rooms_d.readline().rstrip(), rooms_d.readline().rstrip(), rooms_d.readline().rstrip(), rooms_d.readline().rstrip())
                if i == 2 and j == 0:
                    rooms_in.append(Room(rooms_desc[0], rooms_desc[1], j, i, [], Quest(minigames.tic_tac_toe), None))

                elif i == 1 and j == 0:
                    rooms_in.append(Room(rooms_desc[0], rooms_desc[1], j, i, [], Quest(minigames.hangman), None))

                elif i == 0 and j == 0:
                    rooms_in.append(Room(rooms_desc[0], rooms_desc[1], j, i, [], Quest(minigames.guess_number), None))

                elif i == 2 and j == 1:
                    rooms_in.append(Room(rooms_desc[0], rooms_desc[1], j, i, [], Quest(minigames.what_is_it), None))

                elif i == 1 and j == 1:
                    rooms_in.append(Room(rooms_desc[0], rooms_desc[1], j, i, [], Quest(minigames.rock_paper_scissors), None))

                elif i == 0 and j == 1:
                    rooms_in.append(Room(rooms_desc[0], rooms_desc[1], j, i, [], None, Enemy(
                        "troll", {"health": 200, "strength": 50}
                    )))

    if lvl_no == 2:
        for i in range(3):
            rooms_in = []
            for j in range(2):
                rooms_desc = (rooms_d.readline().rstrip(), rooms_d.readline().rstrip(), rooms_d.readline().rstrip(), rooms_d.readline().rstrip(), rooms_d.readline().rstrip())
                if i == 2 and j == 0:
                    rooms_in.append(Room(rooms_desc[0], rooms_desc[1], j, i, [], Quest(minigames.tic_tac_toe), None))

                elif i == 1 and j == 0:
                    rooms_in.append(Room(rooms_desc[0], rooms_desc[1], j, i, [], Quest(minigames.hangman), None))

                elif i == 0 and j == 0:
                    rooms_in.append(Room(rooms_desc[0], rooms_desc[1], j, i, [], Quest(minigames.guess_number), None))

                elif i == 2 and j == 1:
                    rooms_in.append(Room(rooms_desc[0], rooms_desc[1], j, i, [], Quest(minigames.what_is_it), None))

                elif i == 1 and j == 1:
                    rooms_in.append(Room(rooms_desc[0], rooms_desc[1], j, i, [], Quest(minigames.rock_paper_scissors), None))

                elif i == 0 and j == 1:
                    rooms_in.append(Room(rooms_desc[0], rooms_desc[1], j, i, [], None, Enemy(
                        "troll", {"health": 200, "strength": 50}
                    )))


        rooms_out.append(rooms_in)
    return rooms_out