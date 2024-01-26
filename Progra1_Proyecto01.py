#Primer Proyecto de Programacion 1

#Se declaran las variables del menu principal
mainmenuOP = ""

#Imprime el menu
print("   [Primer Proyecto de Programación 1]")
print("      *Crimcat*")
for i in range(2):
    print(" ")

menutext = """
----------[MENÚ]------------------------------------------------------------------
| Digite el número correspondiente a una de las siguientes opciones:             |
|                                                                                |
| (1) Convertir un número decimal a binario.                                     |
|                                                                                |
| (2) Convertir un número binario a decimal.                                     |
|                                                                                |
| (3) Encontrar el segundo número más grande de una lista.                       |
|                                                                                |
| (4) Verificar si una cadena determinada es una dirección de email válida.      |
|                                                                                |
| (5) Generar una contraseña aleatoria de una longitud determinada.              |
|                                                                                |
| (6) Comprobar si un año determinado es bisiesto.                               |
|                                                                                |
| (7) Eliminar elementos duplicados de una lista.                                |
|                                                                                |
| (8) Imprimir la tabla de multiplicar de un número dado.                        |
----------------------------------------------------------------------------------
"""
print(menutext)

#Le pide al usuario que digite el numero correspondiente a la accion que desea realizar
mainpaso = 0 #Variable que determina el paso del proceso del menu en el que se encuentra el usuario

while mainpaso == 0:
    mainmenuOP = input("Digite el número de la acción que desea ejecutar: ")
    maintipo = mainmenuOP.isnumeric()
    if maintipo == True:
        if int(mainmenuOP) >= 1 and int(mainmenuOP) <= 8:
            mainpaso = 1
        else:
            print("Valor no válido. Inténtelo de nuevo.")
            mainpaso = 0
    else:
        print("Valor no válido. Inténtelo de nuevo.")
        mainpaso = 0


#Declara las funciones de los ejercicios
def EJ01():
    #Declara las variables de la función EJ01
    paso = 0
    
    #Declara la función que realiza la conversión
    def getbinary(numdeci):
        bina = ""
        pesos = [128, 64, 32, 16, 8, 4, 2, 1]
        for pesobit in pesos:
            if int(pesobit) <= int(numdeci):
                bina += "1"
                numdeci = numdeci - pesobit
            else:
                bina += "0"
        return bina
    #Le solicita al usuario el valor que desea convertir a binario
    while paso == 0:
        decim = input("Digite el valor decimal entre 0-255 que desea convertir a binario: ")
        decimtipo = decim.isnumeric()
        if decimtipo == True:
            if int(decim) > -1 and int(decim) < 256:
                paso = 1
                numconverted = getbinary(int(decim))
            else:
                print("Debe ser un número entre 0-255. Inténtelo de nuevo.")
        else:
            print("Valor no válido. Inténtelo de nuevo")
    #Imprime los resultados
    print(decim, " convertido a binario es ", numconverted)

def EJ02():
    #Declara las variables de la función EJ02
    paso = 0
    #Declara una función para verificar que el número sea binario
    def veribinary(numbi):
        try:
            #Intenta convertir el número a entero en base 2
            int(numbi, 2)
            return True
        except ValueError:
            #Si hay un error al convertir, significa que no es un número binario
            return False
    
    #Le solicita al usuario un valor binario
    while paso == 0:
        bina = input("Digite un valor binario: ")
        binatipo = bina.isnumeric()
        if binatipo == True and veribinary(bina) == True:
            paso = 1
        else:
            print("Valor no válido. Inténtelo de nuevo.")
    #Realiza la conversión de binario a decimal
    numdeci = int(bina, 2)

    #Imprime el resultado
    print(bina, " convertido a decimal es ", numdeci)

def EJ03():
    #Declara las variables de la función EJ03
    paso = 0
    num_lista = []
    datotal = 10

    #Le solicita al usuario los números que desea introducir en la lista
    while paso == 0:
        print("Espacios de la lista disponibles: ", datotal)
        num = input("Inserte un número para agregar a la lista: ")
        numtipo = num.isnumeric()
        
        if numtipo == True:
            datotal -= 1
            num_lista.append(num)
        elif numtipo == False:
            print("Ese no es un número. Inténtelo de nuevo.")
        if datotal <= 0:
            paso = 1
            num_lista.sort() #sort ordena la lista de menor a mayor
            secondmax = num_lista[8]
    
    #Da los resultados
    print(num_lista)
    print("El segundo número más grande de esta lista es el ", secondmax)

def EJ04():
    #Declara las variables de la función EJ04
    import re
    paso = 0
    
    #Le solicita al usuario un correo electrónico
    while paso == 0:
        email = input("Inserte un correo electrónico: ")
        tipoemail = email.isnumeric() #Variable que ayuda a determinar si el tipo de dato que otorga el usuario es string
        if tipoemail == False:
            paso = 1
        elif tipoemail == True:
            print("Ese no es un correo electrónico. Inténtelo de nuevo")
    
    #Determina los valores del texto dado para determinar si es un correo electrónico válido
    arrobas = email.count("@")
    thecoms = email.count(".com")
    
    #Verifica si el correo electrónico que otorgó el usuario es válido
    if arrobas == 1 and thecoms == 1:
        name, dominio = email.split("@") #Divide el nombre de usuario y el dominio
        if len(dominio) > 4:
            print("EL correo electrónico ", email, " es válido.")
        else:
            print("El correo electrónico ", email, " no es válido.")
    else:
        print("El correo electrónico ", email, " no es válido.")  

def EJ05():
    #Declara las variables de la función EJ05
    chars = "QWERTYUIOPASDFGHJKLÑZXCVBNMqwertyuiopasdfghjklñzxcvbnmÉËÚÜÍÏÓÖÁÄéëúüíïóöáä1234567890@#$_&-+()/*':;!?~`|•√π÷×§∆£€₡₲^°=%©®™✓[]$♪£¢¥₱₹;ςερτυθιοπασδφγηξκλζχψωβνμあかさたなはまらやйцукенгшщзхфывапролджэячсмитьбюЙЦУКЕНГШЩЗХФЫВАПРОЛДЖЭЯЧСМИТЬБЮΕΡΤΥΘΙΟΠΑΣΔΦΓΗΞΚΛΖΧΨΩΒΝΜ "
    import random
    import string
    paso = 0

    #Le solicita al usuario la longitud de la contraseña que desea generar
    while paso == 0:
        largo = input("Ingrese la longitud que desea para su contraseña: ")
        largotipo = largo.isnumeric() #Variable que ayuda a determinar si los datos que ingresa el usuario son numéricos
        if largotipo == True:
            if int(largo) <= len(chars) and int(largo) > 0:
                paso = 1
            else:
                print("La longitud tiene que ser menor a ", len(chars) + 1, " y mayor a 0")
        elif largotipo == False:
            print("Debe ingresar un valor numérico.")
    
    #Genera la contraseña
    contrasena = random.sample(chars, int(largo))

    #Le presenta la contraseña generada al usuario
    print("Aquí está la contraseña que se ha generado: ", "".join(contrasena))

def EJ06():
    #Declara las variables de la función EJ06
    paso = 0

    #Le solicita al usuario el año que desea verificar
    while paso == 0:
        year = input("Ingrese el año que desea ver si es bisiesto: ")
        yeartipo = year.isnumeric()
        if yeartipo == True:
            paso = 1
        elif yeartipo == False:
            print("Ese no es un valor válido. Inténtelo de nuevo.")
    
    #Verifica si el año es bisiesto o no
    if (int(year) % int(4) == int(0) and int(year) % int(100) != int(0)) or (int(year) % int(400) == int(0)):
        print(year, " es un año bisiesto.")
    else:
        print(year, " no es un año bisiesto.")

def EJ07():
    #Declara las variables para la función EJ07
    paso = 0
    dupli_lista = []
    datotal = 10

    #Le solicita al usuario los elementos que desea añadir a la lista
    while paso == 0:
        print("Espacios disponibles en la lista: ", datotal)
        elem = input("Inserte el elemento que desea introducir en la lista: ")
        datotal -= 1
        if datotal > 0:
            dupli_lista.append(elem)
        else:
            print("Todos los espacios de la lista se encuentran ocupados.")
            paso = 1
    
    #Elimina los elementos duplicados de la lista
    if len(dupli_lista) == len(set(dupli_lista)):
        print("No se encontraron elementos duplicados en la lista")
        print(dupli_lista)
    else:
        dupli_conjunto = set(dupli_lista)
        dupli_lista = list(dupli_conjunto)
        print("Se han eliminado los elementos duplicados de la lista. Ahora esta se encuentra de esta forma:")
        print(dupli_lista)

def EJ08():
    #Delcara las variables de la funcion EJ08
    multires = 0 #Resultado de la multiplicacion
    paso = 0
    #Le solicita al usuario el numero del cual quiere saber la tabla de multiplicacion
    while paso == 0:
        numbase = input("Digite el número del cual desea ver la tabla de multiplicación: ")
        tiponum = numbase.isnumeric() #Varaible que ayuda a verificar el tipo de dato del numbase
        if tiponum == True:
            paso = 1
        elif tiponum == False:
            print("Valor no válido. Inténtelo de nuevo")
    
    #Saca los valores de la tabla de multiplicacion
    for i in range(11):
        mul = i
        multires = int(numbase) * int(mul)
        print(numbase, " x ", mul, " = ", multires)

#Define una función para cerrar el programa
def exit():
    #Declara las variables de la función exit
    paso = 0
    while paso == 0:
        salir = input("Digite X para cerrar el programa [X]")
        if salir == "X":
            paso = 1
        else:
            print("Valor no válido. Inténtelo de nuevo.")

#Verifica cual fue la accion que eligio el usuario y la ejecuta
match int(mainmenuOP):
    case 1:
        print("[Convertir un número decimal a binario]")
        EJ01()
    case 2:
        print("[Convertir un número binario a decimal]")
        EJ02()
    case 3:
        print("[Encontrar el segundo número más grande de una lista]")
        EJ03()
    case 4:
        print("[Verificar si una cadena determinada es una dirección de email válida]")
        EJ04()
    case 5:
        print("[Generar una contraseña aleatoria de una longitud determinada]")
        EJ05()
    case 6:
        print("[Comprobar si un año determinado es bisiesto]")
        EJ06()
    case 7:
        print("[Eliminar elementos duplicados de una lista]")
        EJ07()
    case 8:
        print("[Imprimir la tabla de multiplicar de un número dado]")
        EJ08()

#Termina el programa
adios = """
 _____                     _                                                                         _                                                                    
|  __ \                   (_)                                                                       | |                                                                   
| |  \/ _ __   __ _   ___  _   __ _  ___   _ __    ___   _ __   _   _  ___   __ _  _ __    ___  ___ | |_   ___   _ __   _ __   ___    __ _  _ __   __ _  _ __ ___    __ _ 
| | __ | '__| / _` | / __|| | / _` |/ __| | '_ \  / _ \ | '__| | | | |/ __| / _` || '__|  / _ \/ __|| __| / _ \ | '_ \ | '__| / _ \  / _` || '__| / _` || '_ ` _ \  / _` |
| |_\ \| |   | (_| || (__ | || (_| |\__ \ | |_) || (_) || |    | |_| |\__ \| (_| || |    |  __/\__ \| |_ |  __/ | |_) || |   | (_) || (_| || |   | (_| || | | | | || (_| |
 \____/|_|    \__,_| \___||_| \__,_||___/ | .__/  \___/ |_|     \__,_||___/ \__,_||_|     \___||___/ \__| \___| | .__/ |_|    \___/  \__, ||_|    \__,_||_| |_| |_| \__,_|
                                          | |                                                                   | |                   __/ |                               
                                          |_|                                                                   |_|                  |___/                                
"""
print(adios)
exit()