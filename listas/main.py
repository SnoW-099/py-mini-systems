def calculadora(n1,n2,op):
    if op == "+":
        return n1+n2
    elif op == "-":
        return n1-n2
    elif op == "*":
        return n1*n2
    elif op == "/":
        if n2 == 0:
            return "No se puede dividir entre 0, usa otro numero"
        else:
            return n1 / n2

    else:
        return "Error de sintaxis, elige un operador valido"
    
while True:    
    op = input("Con que operador quieres trabajar?(-,+,*,/) o escribe salir para terminar: ").lower ()
    if op == "salir":
        break

    n1 = float(input("Dame el primer numero: "))
    n2 = float(input("Dame el segundo numero: "))


    resultado = calculadora(n1,n2,op)
    print("el resultado es: ", resultado)
