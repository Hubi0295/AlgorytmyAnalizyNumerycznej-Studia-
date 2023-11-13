import math
def aproksymacja(n,tabx,taby,wybor):
    wiersz0=[]
    wiersz1=[]
    if wybor==1:
        for i in range(0,n):
            tabx[i]=math.floor(1/tabx[i])
    if wybor == 2:
        for i in range(0, n):
            taby[i] = math.log(taby[i])
    wiersz0.append(n)
    wiersz0.append(sum(tabx))
    wiersz0.append(sum(taby))
    wiersz1.append(sum(tabx))
    suma=0
    for x in tabx:
        suma+=x*x
    wiersz1.append(suma)
    suma=0
    for i in range(0,n):
        suma+=tabx[i]*taby[i]
    wiersz1.append(suma)
    W=wiersz0[0]*wiersz1[1]-(wiersz0[1]*wiersz1[0])
    Wa0=wiersz0[2]*wiersz1[1]-(wiersz0[1]*wiersz1[2])
    Wa1=wiersz0[0]*wiersz1[2]-(wiersz0[2]*wiersz1[0])
    a=Wa1/W
    b=Wa0/W
    if wybor==0 or wybor==1:
        print("funkcja jest postaci "+str(a),end="")
        if wybor==1:
            print("/",end="")
        print("x",end=" ")
        if b<0:
            print(b)
        else:
            print("+ "+str(b))
    if wybor==2:
        print("funkcja jest postacji e^"+str(a)+"x *e^"+str(b))
def main():
    liczbaWezlow = int(input("Podaj liczbe węzółow: "))
    tabx=[]
    taby=[]
    print("Wcisnij 0 jesli ma to być funkcja postacji ax+b")
    print("Wciśnij 1 jeśli ma to być funkcja postacji a/x + b")
    print("Wciśnij 2 jeśli ma to być funkcja postacji b*a^x")
    wybor = int(input())
    if wybor==2:
        for i in range(0,liczbaWezlow):
            tabx.append(float(input("Podaj x: ")))
            taby.append(math.pow(math.e,float(input("Podaj y(tylko wykładnik): "))))
    else:
        for i in range(0,liczbaWezlow):
            tabx.append(float(input("Podaj x: ")))
            taby.append(float(input("Podaj y: ")))
    aproksymacja(liczbaWezlow,tabx,taby,wybor)
if __name__ == '__main__':
    main()
