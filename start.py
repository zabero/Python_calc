def dodaj(x, y):
    return x + y

def odejmij(x, y):
    return x - y

def pomnoz(x, y):
    return x * y

def podziel(x, y):
    if y == 0:
        return "Błąd! Dzielenie przez zero."
    else:
        return x / y

while True:
    print("\nOpcje:")
    print("Wpisz 'dodaj' aby dodać dwie liczby")
    print("Wpisz 'odejmij' aby odjąć dwie liczby")
    print("Wpisz 'pomnoz' aby pomnożyć dwie liczby")
    print("Wpisz 'podziel' aby podzielić dwie liczby")
    print("Wpisz 'koniec' aby zakończyć program")
    
    wybor_uzytkownika = input(": ")

    if wybor_uzytkownika == "koniec":
        break
    elif wybor_uzytkownika in ('dodaj', 'odejmij', 'pomnoz', 'podziel'):
        num1 = float(input("Wprowadź pierwszą liczbę: "))
        num2 = float(input("Wprowadź drugą liczbę: "))

        if wybor_uzytkownika == "dodaj":
            print("Wynik to", dodaj(num1, num2))
        elif wybor_uzytkownika == "odejmij":
            print("Wynik to", odejmij(num1, num2))
        elif wybor_uzytkownika == "pomnoz":
            print("Wynik to", pomnoz(num1, num2))
        elif wybor_uzytkownika == "podziel":
            print("Wynik to", podziel(num1, num2))
    else:
        print("Nieprawidłowe wejście")
