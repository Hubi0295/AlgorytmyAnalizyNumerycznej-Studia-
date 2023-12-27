import math
import numpy
def MDM3(x,tabM,tabD,tabY):
    tabM = numpy.transpose(tabM)
    tabD = numpy.linalg.inv(tabD)
    tabX = [1] * x
    i = x - 1
    j = x - 1
    tabDy = [1]*x
    a=0
    b=0
    while a<x:
        sum=0
        b=0
        while b<x:
            sum+=tabD[a][b]*tabY[b]
            b+=1
        tabDy[a]=sum
        a+=1
    while i >= 0:
        sum = 0
        j = x - 1
        while j >= 0:
            if (i == j):
                j = j - 1
                continue
            sum = sum + tabX[j] * tabM[i][j]
            j = j - 1
        wynik = (tabDy[i] - sum) / tabM[i][i]
        tabX[i] = wynik
        i = i - 1
    print("Tablica wyników X: ")
    print(tabX,"T")
def MDM2(x,tabM,tab2,tabD):
    tabY = [1] * x
    i = 0
    j = 0
    while i < x:
        sum = 0
        j = 0
        while j < x:
            if (i == j):
                j = j + 1
                continue
            sum = sum + tabY[j] * tabM[i][j]
            j = j + 1
        wynik = (tab2[i] - sum) / tabM[i][i]
        tabY[i] = wynik
        i = i + 1
    print("Macierz Y:")
    print(tabY)
    MDM3(x,tabM,tabD,tabY)
def MDM1(x,matrix,tab2):
    tabD = [[0] * x for _ in range(x)]
    tabM = [[0] * x for _ in range(x)]

    for j in range(x):
        for i in range(j, x):
            sum_d = 0
            for pomoc in range(j):
                sum_d += tabD[pomoc][pomoc] * tabM[i][pomoc] ** 2
            if i == j:
                tabD[i][j] = matrix[i][i] - sum_d
            sum_m = 0
            for pomoc in range(j):
                sum_m += tabM[i][pomoc] * tabM[j][pomoc] * tabD[pomoc][pomoc]
            if i >= j:
                tabM[i][j] = (matrix[i][j] - sum_m) / tabD[j][j]
    print("Macierz D:")
    print(tabD)
    print("Macierz M:")
    print(tabM)
    MDM2(x,tabM,tab2,tabD)
def rozwiazanieUkladu2(tabL,tabY,x):
    tabT = numpy.array(tabL)
    tabT = numpy.transpose(tabT)
    tabX = [1] * x
    i = x-1
    j = x-1
    while i >=0:
        sum = 0
        j = x-1
        while j >=0:
            if (i == j):
                j = j - 1
                continue
            sum = sum + tabX[j] * tabT[i][j]
            j = j - 1
        wynik = (tabY[i] - sum) / tabT[i][i]
        tabX[i] = wynik
        i = i - 1
    print("Tablica wynikowa X:")
    print(tabX,"T")
def rozwiazanieUkladu1(x,tabL,tab2):
    tabY=[1]*x
    i=0
    j=0
    while i<x:
        sum=0
        j=0
        while j<x:
            if(i==j):
                j=j+1
                continue
            sum=sum+tabY[j]*tabL[i][j]
            j=j+1
        wynik=(tab2[i]-sum)/tabL[i][i]
        tabY[i]=wynik
        i=i+1
    print("Macierz Y:")
    print(tabY)
    rozwiazanieUkladu2(tabL,tabY,x)

def macierzTrojkatna(x,tab1,tab2):
    i=0
    j=0
    tabL = [[0]*x for i in range(x)]
    while i<x:
        j=0
        while j<x and j<=i:
            if i==j:
                sum=0
                pomoc=0
                while pomoc<=i-1:
                    sum=sum+math.pow(tabL[i][pomoc],2)
                    pomoc=pomoc+1
                tabL[i][j]=math.sqrt(tab1[i][j]-sum)
            else:
                pomoc=0
                sum=0
                while pomoc<=j-1:
                    sum=sum+tabL[i][pomoc]*tabL[j][pomoc]
                    pomoc=pomoc+1
                tabL[i][j] = (tab1[i][j]-sum)/tabL[j][j]
            j = j + 1
        i=i+1
    print("Macierz L:")
    print(tabL)
    rozwiazanieUkladu1(x,tabL,tab2)
def main():
    x= int(input("Podaj liczbe niewiadomych w rownaniu: "))
    i=0
    j=0
    tab1 = [[0]*x for i in range(x)]
    tab2 = [0]*x
    while i<x:
       while j<x:
            tab1[i][j]=int(input("Podaj wspolczynnik dla x"+str(j)+": "))
            j = j + 1
       j=0
       tab2[i]=int(input("Podaj wynik dla tej linni ukladu rownan: "))
       i=i+1
    wybor= int(input("Podaj ktora metoda chcesz rozwiazac zadanie:\n 1- Rozkład Choleskiego, 2-Rozkład Choleskiego bez pierwiastków kwadratowych"))
    if wybor==1:
        macierzTrojkatna(x,tab1,tab2)
    if wybor==2:
        MDM1(x,tab1,tab2)
if __name__ == '__main__':
    main()
