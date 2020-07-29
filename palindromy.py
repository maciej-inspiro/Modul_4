def palindrom(wyraz):
    """
        Funkcja palindrom, sprawdza czy dany wyraz (string) jest palindromem, tj. słowem, które czytane od lewej do prawej i od prawej do lewej brzmi tak samo (np. kajak)
        Argumenty funkcji:
        wyraz
        W argumentach funkcji naley wpisać wyraz, który funkcja ma sprawdzić pod kątem bycia palindromem np. palindrom("kajak")
    """
    if(wyraz == wyraz[:: - 1]): #string[:: – 1] zwraca stringa w odwrotnej kolejności
        print(bool(1))
    else:
        print(bool(0))


palindrom("potop")
