def funcion():
    import math
    a=input("Dime la x")
    b=input("Dime la y")
    c=input("Dime otro numero")
    raiz=b**2-4*a*c
    if (b**2-4*a*c)<0:
        print "Es de tipo C.No corta con el eje"
    if (b**2-4*a*c)==0:
        print "Es de tipo b. Corta en el punto",-b/2*a
    else:
        print"Es de tipo a. Corta en los puntos",-b+math.sqrt(b**2-4*a*c)/2*a,",",-b-math.sqrt(b**2-4*a*c)/2*a
funcion()
    
