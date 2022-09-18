x=int(input("zadaj cislo: "))
jedna=x%10
desat=x%100//10
if (jedna+desat)%2==0:
    print("posledne 2 cifry su parne")
else:
    print("posledne 2 cifry su neparne")
