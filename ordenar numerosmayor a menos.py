def ordena_numeros():
    n=input("Dime un numero baby:")
    n_cifras=0
    while n>0:
        n=n/10
        n_cifras=n_cifras+1
    return n_cifras
ordena_numeros()


    
    
    
