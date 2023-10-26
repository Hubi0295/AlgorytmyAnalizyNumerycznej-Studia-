def FillingList(a, n):
    i=0
    while i<n:
        a.append(float(input("Podaj: ")))
        i=i+1
def check(a, n, point):
    result=True
    a.sort()
    i=0
    while i<n-1:
        if(a[i]==a[i+1]):
            result=False
        i=i+1
    if(point<a[0] or point>a[n - 1]):
        result=False
    return result
def Neville(tabx, taby, node, point):
    n=len(tabx)
    tabResults=[]
    for i in range(0,len(tabx)):
        tabResults.append(i)
    k=0
    while k<node:
        tabResults[k]=taby[k]
        j=k-1
        while j>=0:
            tabResults[j]= tabResults[j+1] + (tabResults[j+1]-tabResults[j]) * (point - tabx[k]) / (tabx[k] - tabx[j])
            j=j-1
        k=k+1
    return tabResults[0]
def main():
    tabx=[]
    taby=[]
    node=-1
    while node<=1:
        node = int(input("Podaj liczbe węzłów: "))
    i=0
    print("Wypełnianie tabeli X")
    FillingList(tabx, node)
    print("Wypełnianie tabeli Y")
    FillingList(taby, node)
    point=float(input("Podaj punkt: "))
    if check(tabx,node,point):
        print("Wielomian w punkcie "+str(point)+" Wynosi "+ str(Neville(tabx,taby,node,point)))
    else:
        print("Błędne dane")



if __name__ == '__main__':
    main()
