#Autor: Michal Rogala
#Numer albumu: 101723

import random

def get_saying():
    #Funkcja wczytująca plik z przyslowiami i losująca przysłowie do zgadnięcia
    file = open('plik.txt', 'r')
    sayings = file.read().splitlines()
    saying = random.choice(sayings).upper()
    file.close()
    return saying

def replace(answer):
    #Funkcja zastępująca wszysktie litery podkreśleniami (pozostałe znaki pozostają bez zmian)
    answer_hidden = ''
    for i in answer:
        if i.isalpha():
            answer_hidden += '_'
        else:
            answer_hidden += i
    return answer_hidden

def reveal(answer, hidden_saying, guess):
    #Funkcja odkrywająca zgadywaną literę
    guess_index = []
    for i, value in enumerate(answer):
        if value==guess:
            guess_index.append(i)
    lst = list(hidden_saying)
    for j in guess_index:
        lst[j] = guess
    return ''.join(lst)

def get_hint(guessed_letters, answer):
    #Funkcja zwracająca losową literę której użytkownik nie zgadł
    not_guessed = []
    answer_set = set(answer)
    answer_set_alpha_only = filter(str.isalpha, answer_set)
    for i in answer_set_alpha_only:
        if i not in guessed_letters:
            not_guessed.append(i)
    return random.choice(not_guessed)

class Punkt:
	def ustaw_pkt(self, punkt1, punkt2):
		self.punkt1 = punkt1
		self.punkt2 = punkt2
	def drukuj(self):
		return "x=%d, y=%d" %(self.punkt1, self.punkt2)


		


drawings = {0: """
                  _________
                 |         |
                 |         
                 |
                 |
                 |
                 |
                 |
                ---
               """,
            1: """
                  _________
                 |         |
                 |         O
                 |
                 |
                 |
                 |
                 |
                ---
               """,
            2: """
                  _________
                 |         |
                 |         O
                 |         |
                 |
                 |
                 |
                 |
                ---
               """,
            3: """
                  _________
                 |         |
                 |         O
                 |        \\|
                 |
                 |
                 |
                 |
                ---
               """,
            4: """
                  _________
                 |         |
                 |         O
                 |        \\|/
                 |
                 |
                 |
                 |
                ---
               """,
            5: """
                  _________
                 |         |
                 |         O
                 |        \\|/
                 |         |
                 |        /
                 |
                 |
                ---
               """,
            6: """
                  _________
                 |         |
                 |         O
                 |        \\|/
                 |         |
                 |        / \\
                 |
                 |
                ---
               """}

def game():
    errors = 0
    hints = 0
    guessed_letters = []
    saying = get_saying()
    hidden_saying = replace(saying)

    print("""
              -----------------
             | W I S I E L E C |
              -----------------
    """)
    print(drawings[errors])
    print()
    
    while '_' in hidden_saying and errors < 6:
        print("""
    Błędy: %d/6
    Podpowiedzi: %d/3 (aby uzykać podpowiedź wpisz 'PODPOWIEDŹ' podczas zgadywania)
        
    Wykorzystane litery: %s
        
    Hasło: %s""" %(errors, hints, (', '.join(sorted(guessed_letters))), hidden_saying))
        print()
        message = ''
        try:
            guess = input("Wpisz jedną literę/całe hasło: ").upper().strip()
            if guess == '':
                raise ValueError
        except ValueError:
            message = "\tNie podano żadnej litery!"
        print('')
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                message = "\tTa litera została już wykorzystana."
            elif guess not in saying:
                errors += 1
                guessed_letters.append(guess)
                message = "\t\tBłąd!"
            else:
                guessed_letters.append(guess)
                hidden_saying = reveal(saying, hidden_saying, guess)
        elif guess=='':
            pass
        elif guess in ['PODPOWIEDZ', 'PODPOWIEDŹ']:
            if hints < 3:
                hint = get_hint(guessed_letters, saying)
                hidden_saying = reveal(saying, hidden_saying, hint)
                guessed_letters.append(hint)
                hints += 1
            else:
                message = "\tWykorzystano dopuszczalną liczbę podpowiedzi."
        
        elif guess == saying or guess == saying.replace(',', ''):
            hidden_saying = saying
        elif guess.replace(' ','').replace(',','').isalpha() == False:
            message = "\tProgram przyjmuje tylko litery/całe hasło."
        elif guess != saying:
            errors += 1
            message = "\t\tBłąd!"
        
        print(drawings[errors])
        print(message)
    p = Punkt()    
    if '_' not in hidden_saying:
        print("\nWygrałeś! '%s' to zgadywane hasło!\n" %hidden_saying)
        p.ustaw_pkt(6,4)
        print(p.drukuj())
    else:
        print("\nPrzegrałeś - 6 błędów. Zgadywane hasło to '%s'.\n" %saying)

game()

