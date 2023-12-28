def MetodaZmodyfikowanaEulera(n,b):
    x=0
    y=1
    h=(b-x)/n
    i=0
    while i<n:
        y=y+h*(2*((x+0.5*h)*(y+0.5*h*(2*x*y))))
        x=x+h
        i+=1
    return round(y,5)
def MetodaHeuna(n,b):
    h=(b-1)/n
    y=2
    x=1
    i=0
    while i<n:
        y=y+0.5*h*((y/pow(x,2))+((y+h*(y/pow(x,2)))/pow(x+h,2)))
        x=x+h
        i+=1
    return round(y,5)
def MetodaEulera(n,b):
    h=(b-0)/n
    i=0
    x=0
    y=3
    while i<n:
        y=y+h*(pow(y,2)/(x+1))
        x=x+h
        i+=1
    return round(y,3)
def main():
    print("Laboratorium 14\n")

    print("_______________________________________________")
    print("P1 - Metoda Eulera:\ny'=y^2/(x+1)\ny(0)=3")
    print("\nWE\t n=5 \n\t b=1")
    print("WY\t f(1)="+str(MetodaEulera(5,1)))
    print("_______________________________________________")

    print("\nP2 - Metoda Heuna \ny'=y/x^2\ny(1)=2")
    print("\nWE\t n=2 \n\t b=1.5")
    print("WY\t f(1.5)="+str(MetodaHeuna(2, 1.5)))
    print("_______________________________________________")


    print("\nP3 - Metoda zmodyfikowana Eulera \ny'=2xy \ny(0)=1")
    print("\nWE\t n=2 \n\t b=0.5")
    print("WY\t f(0.5)="+str(MetodaZmodyfikowanaEulera(2,0.5)))
    print("_______________________________________________")

if __name__ == '__main__':
    main()
