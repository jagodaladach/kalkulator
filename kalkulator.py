def kalkulator():
    print("Prosty kalkulator")
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")

    wybor = input("Wpisz numer operacji (1/2/3/4): ")

    if wybor in ('1', '2', '3', '4'):
        try:
            a = float(input("Podaj pierwszą liczbę: "))
            b = float(input("Podaj drugą liczbę: "))
        except ValueError:
            print("Błąd: wpisz poprawne liczby.")
            return

        if wybor == '1':
            print(f"Wynik: {a} + {b} = {a + b}")
        elif wybor == '2':
            print(f"Wynik: {a} - {b} = {a - b}")
        elif wybor == '3':
            print(f"Wynik: {a} * {b} = {a * b}")
        elif wybor == '4':
            if b != 0:
                print(f"Wynik: {a} / {b} = {a / b}")
            else:
                print("Błąd: nie można dzielić przez zero.")
    else:
        print("Błąd: nieprawidłowy wybór operacji.")

kalkulator()
