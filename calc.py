import logging
logging.basicConfig(level=logging.DEBUG)

while True:
    operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    a = input("Podaj składnik 1. ")
    if a.isdigit():
        logging.debug("OK")
    else: logging.debug("Podana wartość nie jest liczbą!")
    b = input("Podaj składnik 2. ")
    if b.isdigit():
        logging.debug("OK")
    else: logging.debug("Podana wartość nie jest liczbą!")
    if operation == "1":
      wynik = float(a)+float(b) #float - liczba rzeczywista, int - liczba całkowita (ang. integer)
      logging.info(f"Dodaję {a}  i {b}")
      print(f'Wynik to:  {wynik}')
    elif operation == "2":
      wynik = float(a)-float(b)
      logging.info(f"Odejmuję {a}  i {b}")
      print(f'Wynik to:  {wynik}')
    elif operation == "3":
      wynik = float(a)*float(b)
      logging.info(f"Mnozę {a}  i {b}")
      print(f'Wynik to:  {wynik}')
    elif operation == "4":
      wynik = float(a)/float(b)
      logging.info(f"Dzielę {a}  i {b}")
      print(f'Wynik to:  {wynik}')
    else:
      print("Nie wybrałeś właściciwej opcji. Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")

