import math
def wypelnianieListy(n,tabx,taby,tabPom):
    i=0
    j=0
    while i<n:
        tabx.append(float(input("Podaj x: ")))
        i=i+1
    while j<n:
        taby.append(float(input("Podaj y: ")))
        j=j+1
    i=0
    while i<n:
        tabPom.append(float(input("Podaj wartosci dla wezlow")))
        i=i+1
def Hermite(tabx,taby,wezly,punkt,tabPom):
    tabPamieci=[]
    tabPamieci.append(taby[0])
    for i in range(0,wezly-1):
        tabPamieci.append(i)
    tabPoprzednia=tabPom
    i=0
    licznik=1
    while i<wezly:
        k=i+1
        j=i
        l=0
        while k<wezly:
            if tabx[k]==tabx[l]:
                print("TO MIEJSCE tabK: "+str(tabx[k])+" tabxL: "+str(tabx[l]))
                tabPamieci[k]=taby[k]/math.factorial(licznik)
                print("TABPAMIECI: "+str(tabPamieci[k]))
            else:
                print("tabK: " + str(tabx[k]) + " tabxL: " + str(tabx[l]))
                tabPamieci[k]=((tabPoprzednia[k]-tabPoprzednia[j])/(tabx[k]-tabx[l]))
            k=k+1
            j=j+1
            l=l+1
        print(tabPamieci)
        tabPoprzednia = tabPamieci.copy()
        i=i+1
        licznik=licznik+1

    i=0
    wynik=0
    while i<wezly:
        iloczyn=1
        k=0
        while k<=i-1:
            iloczyn=iloczyn*(punkt-tabx[k])
            k=k+1
        wynik=wynik+(tabPamieci[i]*iloczyn)
        i=i+1
    print(wynik)

def main():
    tabx=[]
    taby=[]
    tabPom=[]
    wezly=-1
    while wezly<=1:
        wezly = int(input("Podaj liczbe węzłów: "))
    i=0
    print("Wypełnianie tabeli")
    wypelnianieListy(wezly,tabx,taby,tabPom)
    print(tabx)
    print(taby)
    print(tabPom)
    punkt=float(input("Podaj punkt: "))
    Hermite(tabx,taby,wezly,punkt,tabPom)


if __name__ == '__main__':
    main()
