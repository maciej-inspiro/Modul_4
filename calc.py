import logging
logging.basicConfig(level=logging.DEBUG)

def valid(s):
    if not s.replace('.', '').replace('+', '').replace('-', '').isdigit():
        return False
    if s.count('.') > 1:
        return False
    return True

while True: #pętla nieskończona
    operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    a = input("Podaj składnik 1. ")
    print(valid(a)) #weryfikacja czy to co podał uzytkownik jest liczbą
    b = input("Podaj składnik 2. ")
    print(valid(b))
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

