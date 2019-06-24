from player import *
from level import *
from introduction import *

class Game:
    def __init__(self, levels, player):
        self.levels = levels
        self.player = player
        self.current_lvl = 0


    def run(self):

        introduction()
        input("Aby przejść do gry, kliknij ENTER.")
        print(self.player.x, self.player.y)

        while self.player.is_alive():
            print("Aktualnie znajdujesz się w: ", self.player.level.rooms[self.player.y][self.player.x])
            print("\n[gram] Pokaż zadanie do wykonania")
            print("-------------------")
            print("[góra] Idź w górę")
            print("[dół] Idź w dół")
            print("[lewo] Idź w lewo")
            print("[prawo] Idź w prawo")
            print("-------------------")
            print("[mapa] Otwórz mapę")
            print("[koniec] Zakonćz grę")
            print("[level] go to next level")

            command = input().lower()


            if command == "góra":
                self.player.move(command)
            elif command == "dół":
                self.player.move(command)
            elif command == "lewo":
                self.player.move(command)
            elif command == "prawo":
                self.player.move(command)
            elif command == "koniec":
                self.player.stats = {"health":0}
            elif command == "mapa":
                self.player.level.print_map(0, 0)
            elif command == 'level':
                # for room in self.player.level.rooms:
                if self.player.level.is_cleared():
                    self.current_lvl += 1
                    self.player.level = self.levels[self.current_lvl]
                    self.player.x = 0
                    self.player.y = 2
                else:
                    print('nie ukonczyles wszystkich questow na tym poziomie')
            elif command == "gram":
                #if room.quest is None:

                 #   print("W tym pokoju nie ma mini gry.")

                self.player.level.rooms[self.player.y][self.player.x].quest.run()
            elif command == "fight":
                enemy = self.player.level.rooms[self.player.y][self.player.x].enemy
                if enemy is not None:
                    while self.player.is_alive() and enemy.is_alive():
                        self.player.attack(enemy, input('Wybierz rodzaj ataku (siła lub magia): '))
                        enemy.attack(self.player)
                else:
                    print("Aby wykonać walkę przejdź do pokoju ........")
            else:
                print("Zła komenda.")


        print("GAME OVER.")


def main():
    print("""Drogi przybyszu z lądu!\n\nWitaj w grze "Podwodny Skarb"!""")
    name = input("Aby kontynuować, wpisz imię swojego bohatera: ")
    levels = level_gen(2)
    player = Player(name, 0, 2, {"health":100, "strength": 100, "mp": 0, "magic_skills": 50}, levels[0])
    game = Game(levels, player)
    game.run()



main()