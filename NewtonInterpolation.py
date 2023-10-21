def wypelnianieListy(a,n):
    i=0
    while i<n:
        a.append(float(input("Podaj: ")))
        i=i+1
def check(a,n,punkt):
    result=True
    i=0
    while i<n-1:
        if(a[i]>=a[i+1]):
            result=False
        i=i+1
    if(punkt<a[0] or punkt>a[n-1]):
        result=False
    return result
def Newton(tabx,taby,wezly,punkt):
    tabPamieci=[]
    tabPamieci.append(taby[0])
    for i in range(0,wezly-1):
        tabPamieci.append(i)
    tabPoprzednia=taby
    i=0
    while i<wezly:
        k=i+1
        j=i
        l=0
        while k<wezly:
            tabPamieci[k]=((tabPoprzednia[k]-tabPoprzednia[j])/(tabx[k]-tabx[l]))
            k=k+1
            j=j+1
            l=l+1
        tabPoprzednia = tabPamieci.copy()
        i=i+1

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
    wezly=-1
    while wezly<=1:
        wezly = int(input("Podaj liczbe węzłów: "))
    i=0
    print("Wypełnianie tabeli X")
    wypelnianieListy(tabx,wezly)
    print("Wypełnianie tabeli Y")
    wypelnianieListy(taby,wezly)
    punkt=float(input("Podaj punkt: "))
    if check(tabx,wezly,punkt):
        Newton(tabx,taby,wezly,punkt)



if __name__ == '__main__':
    main()
