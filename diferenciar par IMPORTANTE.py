def diferenciar_par():
    n=input("Dime un numero")
    pares=0
    while n>1:
        x=n%10
        if x%2==0:
            pares=pares+1
        n=n/10
    print "El numero tiene",pares,"pares"
diferenciar_par()
