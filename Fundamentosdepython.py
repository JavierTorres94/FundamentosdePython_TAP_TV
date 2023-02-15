#Esto es un comentario.

def nuevoTema(tema):
    print("\n =========",tema,"============\n")


if __name__ == "__main__":
    print("====Operadores Aritmeticos====")
    print("Operador de division entera (10 // 3): ", 10//3)
    print("Operador de potencias (5 ** 5):", 5**5)
    print("Operador de cambio de signo (-5): ",-5)
    #Actividad: Mostra las tablas de verdad de los operadores logicos and not or    
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

    nuevoTema("Enteros")
    w=105
    x=233243423423
    y=-21332131
    z=0b00101010101
    h= 0xffa #Entero en hecadecimal

    print(w,type(w))
    print(x,type(x))
    print(y,type(y))
    print(z,type(z))
    print(h,type(h))


    nuevoTema("Flotantes")
    x=1297.5
    print(x, type(x))
    y=0.32432423
    print(y, type(y))

    nuevoTema("Numero Complejos")
    x=-46j
    y=32+45j
    z=2j

    print(x,type(x))
    print(y,type(y))
    print(z,type(z))

    nuevoTema("Listas")
    a=[10,20.5,"PythonList"]
    print(a)
    a=["lista2",45,16.3j]
    print(a)
    print(a,[2])

    nuevoTema("Tuplas") #Las Tuplas son estables
    t=(25,"Tupla",5.6)
    print(t)
    print(t[1])
    #t[0]="Modificado" Las tuplas no permiten que se rescriban los datos
    #print(t)

    nuevoTema("Los conjuntos")
    c = {50, 20, 10, 4, 8, 50} #Los conjuntos usan las llaves
    print(c)

    #json con una clave se almacena un nombre y un valor

    d={1:"Valor2","2":45}
    print(d)
    print(d["2"])
    print(d[1])

    nuevoTema("Cadena") #segun las comillas es el texto que puedes escribir, y el tabulador recorre el texto
    cadena1="cadena entre comillas dobles"
    print(cadena1)
    cadena2='cadena entre comillas sencillas'
    print(cadena2)
    cadena3='''cadena de 
    varias
    lineas'''
    print(cadena3)
