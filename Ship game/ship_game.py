import random

class GraWOkrety:
    def __init__(self):
        # Inicjalizacja gry - plansza 10x10, dwie plansze dla każdego gracza, długości statków.
        self.rozmiar_planszy = 10
        self.plansza1 = [[' ' for _ in range(self.rozmiar_planszy)] for _ in range(self.rozmiar_planszy)]
        self.plansza2 = [[' ' for _ in range(self.rozmiar_planszy)] for _ in range(self.rozmiar_planszy)]
        self.dlugosci_statkow = [2, 3, 3, 4, 5]

    def resetuj_plansze(self):
        # Zresetuj obie plansze graczy do stanu początkowego (puste).
        self.plansza1 = [[' ' for _ in range(self.rozmiar_planszy)] for _ in range(self.rozmiar_planszy)]
        self.plansza2 = [[' ' for _ in range(self.rozmiar_planszy)] for _ in range(self.rozmiar_planszy)]
    
    def wstaw_statki(self):
        # Umieszczanie statków losowo na jednej z plansz.
        kierunki = ["poziomo", "pionowo"]

        dlugosci_statkow = self.dlugosci_statkow.copy()

        liczba_statkow = len(dlugosci_statkow)

        while liczba_statkow > 0:
            kierunek = random.choice(kierunki)
            dlugosc = random.choice(dlugosci_statkow)
            x = random.randint(0, self.rozmiar_planszy - 1)
            y = random.randint(0, self.rozmiar_planszy - 1)

            mozna_wstawic = True

            if kierunek == "poziomo":
                # Sprawdzenie, czy statek może być umieszczony poziomo bez wyjścia poza planszę lub nachodzenia na inne statki.
                if y + dlugosc > self.rozmiar_planszy:
                    mozna_wstawic = False
                else:
                    for i in range(dlugosc):
                        if self.plansza2[x][y + i] != ' ':
                            mozna_wstawic = False
                            break
            elif kierunek == "pionowo":
                # Sprawdzenie, czy statek może być umieszczony pionowo bez wyjścia poza planszę lub nachodzenia na inne statki.
                if x + dlugosc > self.rozmiar_planszy:
                    mozna_wstawic = False
                else:
                    for i in range(dlugosc):
                        if self.plansza2[x + i][y] != ' ':
                            mozna_wstawic = False
                            break

            # Jeśli statek może być umieszczony, zaktualizuj planszę i zmniejsz liczbę pozostałych statków.
            if mozna_wstawic:
                if kierunek == "poziomo":
                    for i in range(dlugosc):
                        self.plansza2[x][y + i] = 'X'
                else:
                    for i in range(dlugosc):
                        self.plansza2[x + i][y] = 'X'
                liczba_statkow -= 1
                dlugosci_statkow.remove(dlugosc)

    def czy_mozna_wstawic(self, wspolrzedne):
        # Sprawdź, czy wprowadzone współrzędne są poprawne i wykonaj strzał na planszy przeciwnika.
        if len(wspolrzedne) == 2 and wspolrzedne[0].isalpha() and wspolrzedne[1].isdigit():
            x = ord(wspolrzedne[0]) - ord('A')
            y = int(wspolrzedne[1]) - 1
            if 0 <= x < 10 and 0 <= y < 10:
                if self.plansza1[x][y] == ' ':
                    self.strzal(x, y)
                else:
                    print("STRZAŁ JUŻ ZOSTAŁ ODDANY W TYM MIEJSCU!")
            else:
                print("BŁĘDNE WSPOŁRZĘDNE!")
        elif len(wspolrzedne) == 3 and wspolrzedne[0].isalpha() and wspolrzedne[1:].isdigit():
            x = ord(wspolrzedne[0]) - ord('A')
            y = int(wspolrzedne[1:]) - 1
            if 0 <= x < 10 and 0 <= y < 10:
                if self.plansza1[x][y] == ' ':
                    self.strzal(x, y)
                else:
                    print("STRZAŁ JUŻ ZOSTAŁ ODDANY W TYM MIEJSCU!")
            else:
                print("BŁĘDNE WSPOŁRZĘDNE!")
        else:
            print("BŁĘDNE DANE!")

    def strzal(self, x, y):
        # Wykonaj strzał i zaktualizuj planszę gracza na podstawie wyniku.
        if self.plansza2[x][y] == 'X':
            self.plansza1[x][y] = 'X'
        else:
            self.plansza1[x][y] = 'O'

    def wstaw_strzal(self):
        # Pobierz od użytkownika współrzędne do wykonania strzału.
        wspolrzedne = input("Podaj wspołrzędne twojego strzału (Bez spacji np: \"A1\"): ").upper()
        print()

        self.czy_mozna_wstawic(wspolrzedne)

    def koniec_gry(self):
        # Sprawdź, czy wszystkie statki przeciwnika zostały zatopione.
        for i in range(self.rozmiar_planszy):
            for j in range(self.rozmiar_planszy):
                if self.plansza2[i][j] == 'X' and self.plansza1[i][j] != 'X':
                    return False
        return True


class GraWOkrtyInt(GraWOkrety):
    def rozpocznij_gre(self):
        # Rozpocznij pętlę gry.
        gra = True

        while gra:
            self.wstaw_statki()
            
            # Wyświetl planszę gracza.
            print("\n\t\tTWOJA PLANSZA:")
            self.wyswietl_plansze(1)
            print("\nO - Pudło\nX - Trafiony")

            tura = 1

            while True:
                # Pętla tury gracza.
                print(f"\n|||||||||||||||||||||||||||||||||||||||||||||||||| TURA {tura} ||||||||||||||||||||||||||||||||||||||||||||||||||\n")

                self.wstaw_strzal()

                # Wyświetl zaktualizowaną planszę gracza.
                print("\n\t\tTWOJA PLANSZA:")
                self.wyswietl_plansze(1)
                print("\nO - Pudło\nX - Trafiony")

                if self.koniec_gry():
                    # Sprawdź, czy wszystkie statki przeciwnika zostały zatopione, aby zakończyć grę.
                    print("\n|||||||||||||||||||||||||||||||||||||||||||||||||||||||")
                    print("\nGRATULACJE UŻYTKOWNIKU!!! ZATOPIŁEŚ WSZYSTKIE STATKI!!!")
                    print("\n|||||||||||||||||||||||||||||||||||||||||||||||||||||||")
                    break

                tura += 1

            decyzja = input("\nCzy chcesz zagrać jeszcze raz? (Wpisz \"Tak\" lub \"Nie\"): ").upper()

            pytanie = True

            while pytanie:
                if decyzja == "TAK":
                    pytanie = False
                elif decyzja == "NIE":
                    print("\nKONIEC GRY!")
                    pytanie = False
                    gra = False
                else:
                    decyzja = input("\nNieprawidłowa odpowiedź. (Wpisz \"Tak\" lub \"Nie\"): ").upper()

            self.resetuj_plansze()

    def wyswietl_plansze(self, plansza):
        # Wyświetl planszę gry dla gracza lub komputera na podstawie parametru 'plansza'.
        print("   ", end=" ")
        for i in range(1, 11):
            print(f" {i} ", end=" ")
        print()

        if plansza == 1:
            # Wyświetl planszę gracza.
            for i in range(self.rozmiar_planszy):
                print(f" {chr(65 + i)} ", end="")
                for j in range(self.rozmiar_planszy):
                    print(f"| {self.plansza1[i][j]} ", end="")
                print("|")
        elif plansza == 2:
            # Wyświetl planszę komputera.
            for i in range(self.rozmiar_planszy):
                print(f" {chr(65 + i)} ", end="")
                for j in range(self.rozmiar_planszy):
                    print(f"| {self.plansza2[i][j]} ", end="")
                print("|")


if __name__ == "__main__":
    # Rozpocznij grę, tworząc instancję klasy 'GraWOkrtyInt' i wywołując metodę 'rozpocznij_gre'.
    gra = GraWOkrtyInt()
    gra.rozpocznij_gre()