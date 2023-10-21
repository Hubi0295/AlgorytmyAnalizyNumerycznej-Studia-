import math
def print_hi(name):
    lista=[]
    liczba = (234.13)
    podstawa = int(input("Podaj podstawe"))
    dokladnosc = int(input("Podaj dokladnosc"))
    liczba= math.floor(liczba*pow(podstawa,dokladnosc))
    while liczba!=0:
        lista.append(liczba%2)
        liczba=liczba//2
    lista.reverse()
    licznik=len(lista)
    for li in lista:
        print(li,end="")
        licznik=licznik-1
        if licznik==dokladnosc:
            print(",",end="")
