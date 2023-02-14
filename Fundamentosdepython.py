#Esto es un comentario.

def nuevoTema(tema):
    print("\n =========",tema,"============\n")


if __name__ == "__main__":
    print("====Operadores Aritmeticos====")
    print("Operador de division entera (10 // 3): ", 10//3)
    print("Operador de potencias (5 ** 5):", 5**5)
    print("Operador de cambio de signo (-5): ",-5)
    
    print("====Operadores logicos====")
    print("Operador and (True and False):", True and False)
    print("Operador and (False and True):", True and True)
    print("Operador and (False and False): ", False and False)
    print("Operador and (True and True):", True and True)

    print("Operador or (True or False):", True or False)
    print("Operador or (False or True):", True or True)
    print("Operador or (False or False): ", False or False)
    print("Operador or (True or True):", True or True)

    print("Operador not (not true):", not True)
    print("Operador not (not false):", not False)

    print("operador == (2==2):", 2==2)
    print("operador > (2>1):", 2>1)
    print("operador >= (3>= 3):", 3>=3)
    print("operador < (2<1):", 2<1)
    print("operador <= (3<= 3):", 3<=3)


    nuevoTema("operadores de comparacion")
    print("2==3", 2==3)


    nuevoTema("Variables")
    variable1=10
    _variable2 = 34.2
    Variable3="pepe"
    dos_palabras="Hola"
    dosPalabras="Hello"

    print(variable1,_variable2,Variable3,dos_palabras,dosPalabras)


    a,b,c=98,3.1416,"Bienvenido"
    print(a,b,c)

    

       
    
    #Actividad: Mostra las tablas de verdad de los operadores logicos and not or
    