import math


def Horner(n,a,c):
    i=0
    while i<n:
        k=1
        while k<=n-i:
            a[k]=(a[k-1]*c+a[k])
            k=k+1
        i=i+1
    i=0
    while i<n:
        a[i]=a[i]*math.factorial(n-i)
        i=i+1
    a.reverse()
    i=0
    for licz in a:
        print("wielomian w punkcie "+str(c)+" pochodnej rzedu:"+str(i)+" wynosi"+str(licz))
        i=i+1
def Horner1(n,a,c):
    i=0
    licznik=1
    nowa=[]
    nowa.append(a[0])
    while licznik<=n:
        nowa.append(0)
        licznik=licznik+1
    print("  "+str(a))
    while i<=n:
        w=a[0]
        x=1
        while x<=n:
            w=w*c+a[x]
            nowa[x]=w
            x=x+1
        print(str(c)+"|"+str(nowa)+" Wynik: "+str(nowa[len(nowa)-i-1]*math.factorial(i)))
        a=nowa
        i=i+1
def print_hi(name):
    tablica = [3,3,-2,11]
    liczba=-1
    Horner1(len(tablica)-1,tablica,liczba)
    # Horner(liczba-1,tablica,pierw)
if __name__ == '__main__':
    print_hi('PyCharm')
