a=int(input("zadaj stranu a: "))
b=int(input("zadaj stranu b: "))
c=int(input("zadaj stranu c: "))

if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("trojuholnik je rovnostranny")
    elif a==b or a==c or b==c:
        print("trojuholnik je rovnoramenny")
    else:
        print("trojuholnik je roznostranny")
    if a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+b**2:
        print("trojuhlonik je pravouhly")
    elif a**2>b**2+c**2 or b**2>a**2+c**2 or c**2>a**2+b**2:
        print("trojuholnik je tupouhly")
    else:
        print("trojuholnik je ostrouhly")
else:
    print("trojuholnik neexistuje")

