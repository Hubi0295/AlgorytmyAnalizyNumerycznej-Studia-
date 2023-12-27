import math
import numpy
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
    return tabX
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
    return tabY

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
    return tabL
def main():
    x= int(input("Podaj liczbe niewiadomych w rownaniu: "))
    i=0
    j=0
    tab1 = [[0]*x for i in range(x)]
    print(tab1)
    tab2 = [0]*x
    while i<x:
       while j<x:
            tab1[i][j]=int(input("Podaj wspolczynnik dla x"+str(j)+": "))
            j = j + 1
       j=0
       tab2[i]=int(input("Podaj wynik dla tej linni ukladu rownan: "))
       i=i+1
    roz=rozwiazanieUkladu1(x,macierzTrojkatna(x,tab1,tab2),tab2)
    print(rozwiazanieUkladu2(macierzTrojkatna(x,tab1,tab2),roz,x),"T")
if __name__ == '__main__':
    main()
