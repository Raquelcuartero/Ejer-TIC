def suma(num1,num2):
    resp=num1+num2
    return resp
def resta(num1,num2):
    resp=num1-num2
    return resp1
def multiplicacion(num1,num2):
    resp=num1*num2
    return resp2
def divsion(num1,num2):
    resp=num1/num2
    return resp3

def menu_operacion():
        seguir="SI"
        suma=0
        num1=input("Dime otro numero:")
        num2=input("Dime otro numero:")
        while (seguir=="SI"):
            print"Que deseas hacer con los numeros"
            print"1.Sumarlos"
            print"2.Restarlos"
            print"3.Multiplicarlos"
            print"4.Dividirlos"
            respuesta=input()
            if(respuesta==1):
               suma(num1,num2)
menu_operacion()
