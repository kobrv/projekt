import random

class Quest:
    def __init__(self, mainloop):
        self.mainloop = mainloop
        self.completed = False


    def run(self):
        self.completed = self.mainloop()


def guess_number():

    print("Twoim zadaniem będzie zgadnięcie, jaką liczbę mam na myśli.\nJest to liczba z zakresu od 1 do 100. \nGotowy?")
    number = random.randint(1, 100)
    i = 0
    while int(i) < 10:
        guess = int(input("Podaj liczbę od 1 do 100. "))
        i += 1
        if guess < number:
            print("Podana liczba jest za mała!")
        elif guess > number:
            print("Podana liczba jest za duża!")
        else:
            print("Brawo! moja liczba to", number, "!")
            return True
            break
        print("Ilość ruchów: ", 10 - i)
    if i > 10:
        print("Przegrałeś...")
        return False



def hangman():

    HANGMAN = (
        """
     _________
     |/      |
     |      
     |      
     |       
     |      
     |
    _|___
        """,
        """
     _________
     |/      |
     |      (_)
     |      
     |       
     |      
     |
    _|___
        """,
        """
     _________
     |/      |
     |      (_)
     |       |
     |       
     |      
     |
    _|___
        """,
        """
     _________
     |/      |
     |      (_)
     |      \|
     |       
     |      
     |
    _|___
        """,
        """
     _________
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
    _|___
        """,
        """
     _________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
    _|___
        """,
        """
     _________
     |/      |
     |      (_)
     |      \|/
     |       |
     |     _/ 
     |
    _|___
        """,
        """
     _________
     |/      |
     |      (_)
     |      \|/
     |       |
     |     _/ \_
     |
    _|___
        """)

    loss = len(HANGMAN) - 1
    WORDS = ("ATLANTYDA", "OCEAN", "SKARB", "TAJEMNICA", "ABRAKADABRA")

    word = random.choice(WORDS)
    so_far = "-" * len(word)
    wrong = 0
    used = []

    print("Witaj w grze 'Wisielec'.  Powodzenia!")

    while wrong < loss and so_far != word:
        print(HANGMAN[wrong])
        print("\nWykorzystane litery:\n", used)
        print("\nZagadka:\n", so_far)

        guess = input("\n\nWprowadź literę: ")
        guess = guess.upper()

        while guess in used:
            print("Już wykorzystałeś literę", guess)
            guess = input("Wprowadź literę: ")
            guess = guess.upper()

        used.append(guess)

        if guess in word:
            print("\nBrawo!", guess, "znajduje się w moim słowie!")


            new = ""
            for i in range(len(word)):
                if guess == word[i]:
                    new += guess
                else:
                    new += so_far[i]
            so_far = new

        else:
            print("\nNiestety,", guess, "nie występuje w moim słowie.")
            wrong += 1

    if wrong == loss:
        print(HANGMAN[wrong])
        print("\nPrzegrałeś...")
        return False
    else:
        print("\nOdgadłeś moje słowo!")
        return True

    print("\nMoje słowo to", word)



def tic_tac_toe():

    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    end = False
    used = []

    win_commbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def draw():
        print(board[0], "|", board[1], "|", board[2])
        print("---------")
        print(board[3], "|", board[4], "|", board[5])
        print("---------")
        print(board[6], "|", board[7], "|", board[8])
        print()

    draw()

    def player():
        n = choose_number()
        board[n] = "O"
        used.append(n)

    def computer():
        n = random.randint(0,8)

        board[n] = "X"
        used.append(n)



    def choose_number():
        while True:
            while True:
                a = input("Gdzie chcesz postawić kółko? ")
                try:
                    a = int(a)
                    a -= 1
                    if a in range(0, 9):
                        return a
                    else:
                        print("Podano miejsce poza planszą...")
                        continue
                except ValueError:
                    print("\n To nie jest liczba! Spróbuj jeszcze raz. ")
                    continue

    def check_board():
        count = 0
        for a in win_commbinations:
            if board[a[0]] == board[a[1]] == board[a[2]] == "O":
                print("Wygrałeś!")
                return True

            if board[a[0]] == board[a[1]] == board[a[2]] == "X":
                print("Przegrałeś :(")
                return False

        for a in range(9):
            if board[a] == "X" or board[a] == "O":
                count += 1
            if count == 9:
                print("Remis...")
                return False

    while not end:
        player()
        draw()
        end = check_board()
        if end == True:
            break
        print("Ruch komputera:")
        computer()
        draw()
        end == check_board()
        if end == True:
            break
        print()



def rock_paper_scissors():

    print("\n\nGra polega na zdobyciu 3 punktow w grze w papier/kamień/nożyce.")
    print("ZASADY: Kamień bije nożyce, papier bije kamień, nożyce biją papier.")
    MOVES = ("papier", "kamień", "nożyce")
    score = 0
    while score != 3 and score >= 0:
        choice = input("Twoj ruch: ")
        tries = 0
        for move in MOVES:
            if choice.lower() != move:
                tries += 1
        computer = MOVES[random.randint(0,2)]
        print("Ruch przeciwnika: " + computer)
        if choice.lower() == computer:
            print("Remis!")
        if choice.lower() == "kamień":
            if computer.lower() == "papier":
                print("Tracisz punkt :(")
                score -= 1
            elif computer.lower() == "nożyce":
                print("Zdobywasz punkt!\n")
                score += 1
        if choice.lower() == "papier":
            if computer.lower() == "nożyce":
                print("Tracisz punkt :(")
                score -= 1
            elif computer.lower() == "kamień":
                print("Zdobywasz punkt!\n")
                score += 1
        if choice.lower() == "nożyce":
            if computer.lower() == "kamień":
                print("Tracisz punkt :(")
                score -= 1
            elif computer.lower() == "papier":
                print("Zdobywasz punkt!\n")
                score += 1
        print("Twoj wynik:", score,"\n")
    if score == 3:
        print("Wygrywasz!")
        return True
    else:
        print("Przegrywasz...")
        return False



def what_is_it():

    ananas = ["""          
          \||/
          \||/
        .<><><>.
       .<><><><>.
       '<><><><>'
jgs     '<><><>'""" , "ananas"]
    carrot = ["""  \/_
                 _/        
                (,;)
                (,.)
                (,/
                |/""", "marchewka"]
    spongebob = [
             """      
     .--..--..--..--..--..--.
    .' \  (`._   (_)     _   |
  .'    |  '._)         (_)  |
  \ _.')\      .----..---.   /
  |(_.'  |    /    .-\-.  \  |
  \     0|    |   ( O| O) | o|
   |  _  |  .--.____.'._.-.  |
   \ (_) | o         -` .-`  |
    |    \   |`-._ _ _ _ _\ /
    \    |   |  `. |_||_|   |
    | o  |    \_      \     |     -.   .-.
    |.-.  \     `--..-'   O |     `.`-' .'
  _.'  .' |     `-.-'      /-.__   ' .-'
.' `-.` '.|='=.='=.='=.='=|._/_ `-'.'
`-._  `.  |________/\_____|    `-.'
   .'   ).| '=' '='\/ '=' |
   `._.`  '---------------'
           //___\   //___\
             ||       ||
    LGB      ||_.-.   ||_.-.
            (_.--__) (_.--__)""", "spongebob"]
    mickey = [
             """                    
                    _..-----._
                  .'          '.
                 /              \
                |                ;
                |                 |
                \                 |
                 \               ;
           _..----'             /
         .`-. .-'``'-.       .-'
       .'_   `  _     '.    `'.
      /  _`    _ `      \      \     _...._
   _  | /  \  /  \      |       | .-'      `'.
  / \ | | /|  | /|      |       ;'            \
 |  |_\ \_|/  \_|/      /                      ;
 .\_/  `'-.            /_...._                 |
/          `                  `\               |
|                        __     |             /
 \                       / `   //'.         .'
  '._                  .'     .'   `'-...-'`
     `"'-.,__    ___.-'    .-'
    jgs  `-._````  __..--'`
             ``````""", "myszka miki"]
    words = [ananas, carrot, spongebob, mickey]
    used = []
    #counter = 0
    points = 0
    while True:
        random_num = random.randint(0, 3)
        word = words[random_num][0]
        while word not in used:
            input("Wcisnij enter, by wyswietlic obrazek!")

            print("Twoj obrazek:")
            print(word)
            guess = input("\nCo to jest?: ")
            if guess == words[random_num][1]:
                print("Dobrze! Otrzymujesz punkt!")
                points += 1
            else:
                print("Niestety nie, prawidlowa odpowiedz to " + words[random_num][1] + ".")
            used.append(words[random_num][0])

        #counter += 1
            if points == 3:
                return True
            else:
                return False



def quiz():
    file = open("quiz.txt", "r")
    questions = []
    for line in file:
        x = [file.readline().replace("\n", ""), file.readline().replace("\n", ""), file.readline().replace("\n", ""),
             file.readline().replace("\n", ""), file.readline().replace("\n", ""), file.readline().replace("\n", "")]
        questions.append(x)

    print("Odpowiedz dobrze na wszystkie pytania, aby przejść dalej!")
    number = 0
    n = 0
    input("Gotowy? Naciśnij ENTER.")
    while True:
        print("\nPytanie " + "#" + str(number + 1))
        print(questions[n][0])
        print("A. " + questions[n][1])
        print("B. " + questions[n][2])
        print("C. " + questions[n][3])
        print("D. " + questions[n][4])
        while True:
            guess = input("Prawidłowa odpowiedź: ")
            if guess.upper() == questions[n][5]:
                print("\nDobra odpowiedz!")
                number += 1
                n += 1
                break
            else:
                print("Zła odpowiedź. Spróbuj jeszcze raz.")



def cowsBulls():

    print("\n\nZacznijmy od wyjasnienia zasad. W grze generowana jest 4-cyfrowa liczba. Twoim zadaniem jest ja zgadnac!")
    print("Po kazdej rundzie zgadywania dowiadujesz sie, ile masz krowek, a ile bykow. Dostajesz byka za kazda liczbe")
    print("we wlasciwym miejscu, a kazda krowe za blad. Przyjmujac, ze wylosowana liczba to 4176, przy zgadnieciu")
    print("2186 dostaniesz dwie krowy i dwa byki, a przy 4186 jedna krowe i 3 byki. Jasne? To lecimy!\n")

    number = str(random.randint(1000,9999))
    while True:
        cowsandbulls = [0,0]
        playerGuess = input("Podaj zgadywana liczbe: ")
        if len(playerGuess) != 4:
            print("Liczba musi miec 4 cyfry!")
            continue
        try:
            for i in range(len(number)):
                if number[i] == playerGuess[i]:
                    cowsandbulls[1] += 1
                else:
                    cowsandbulls[0] += 1
        except ValueError:
            print("Nalezy podac liczbe!")
            continue
        print("Krowki:", cowsandbulls[0], "| Byki:", cowsandbulls[1])
        if cowsandbulls[1] == 4:
            return True



def spelling_bee():
    word_1 = ["rzeżucha", "Rzerzucha, żerzuha, rzeżucha, a może żeżucha???"]
    word_2 = ["chihuahua", "cuachua, ciułała, chichuaua, chihuahua...?"]
    word_3 = ["hipochondryk", "chipohondyk? hipochondryk? chipochondyk? hipohondryk?"]
    word_4 = ["sufrażystka", "surfażystka, sufrażystka, surfarzystka, sufrarzystka?"]
    word_5 = ["nowo narodzony", "nowonarodzony, nowo-narodzony, a może nowo narodzony?"]
    word_6 = ["ponaddwuipółmiesięczny", "'ponad dwu i pół miesięczny', 'ponaddwu i pół miesięczny', ponad dwuipółmiesięczny, ponaddwuipółmiesięczny??"]
    words_to_guess = [word_1, word_2, word_3, word_4, word_5, word_6]
    used = []
    points = 0
    while points <=3 :
        random_num = random.randint(0, 5)
        to_guess = words_to_guess[random_num][0]
        while to_guess not in used:
            input("Wcisnij enter, by wyswietlic zagadkę!")
            print("Jak to się pisze?:")
            print(words_to_guess[random_num][1])
            guess = input("\nPrawidłowy zapis: ")
            if guess == words_to_guess[random_num][0]:
                print("Dobrze! Otrzymujesz punkt!")
                points += 1
            else:
                print("Niestety nie, prawidlowa odpowiedz to " + words_to_guess[random_num][0] + ".")
            used.append(words_to_guess[random_num][0])

    if points == 3:
        return True
    else:
        return False




