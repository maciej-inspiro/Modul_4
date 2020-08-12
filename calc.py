import logging
logging.basicConfig(level=logging.DEBUG)
operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
if operation == "1":
    a = input("Podaj składnik 1. ")
    b = input("Podaj składnik 2. ")
    wynik = float(a)+float(b) #float - liczba rzeczywista, int - liczba całkowita (ang. integer)
    logging.info("Dodaję " + a + " i " + b)
    print("Wynik to " + str(wynik))
elif operation == "2":
    a = input("Podaj składnik 1. ")
    b = input("Podaj składnik 2.")
    wynik = float(a)-float(b)
    logging.info("Odejmuję " + a + " i " + b)
    print("Wynik to " + str(wynik))
elif operation == "3":
    a = input("Podaj składnik 1. ")
    b = input("Podaj składnik 2. ")
    wynik = float(a)*float(b)
    logging.info("Mnożę " + a + " i " + b)
    print("Wynik to " + str(wynik))
elif operation == "4":
    a = input("Podaj składnik 1.")
    b = input("Podaj składnik 2.")
    wynik = float(a)/float(b)
    logging.info("Dzielę " + a + " i " + b)
    print("Wynik to " + str(wynik))
