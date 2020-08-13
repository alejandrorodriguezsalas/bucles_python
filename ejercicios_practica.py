#!/usr/bin/env python
'''
Bucles [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

# Variable global utilizada para el ejercicio de nota
notas = [70, 82, -1, 65, 55, 67, 87, 92, -1]

# Variable global utilizada para el ejercicio de temperaturas
temp_dataloger = [12.8, 18.6, 14.5, 20.8, 12.1, 21.2, 13.5, 18.6,
                  14.7, 19.6, 11.2, 18.4]


def ej1():
    print('     Ej1:Comenzamos a ponernos serios!')

    '''
    Realice un programa que pida por consola dos números que representen
    el principio y fin de una secuencia numérica.
    Realizar un bucle "for" que recorra esa secuencia armada con "range"
    y cuente cuantos números ingresados hay, y la sumatoria de todos los números
    Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    sino que va hasta el anterior
    '''

    inicio = int(input('Ingrese el número inicial de la secuencia:  '))
    fin = int(input('Ingerese el número fianl de la secuencia:  '))

    cont = 0
    acum = 0

    for i in range(inicio,fin+1):
        acum += i
        cont += 1

    print("\nLa suamatoría de los núemros dentro de rango es: ",acum)
    print("La cantidad de números dentro del rango es: ",cont)

    # Al terminar el bucle calcular el promedio como:
    # promedio = sumatoria / cantidad_numeros    
    prom = acum / cont
    
    # Imprimir resultado en pantalla
    print('El promedio de la secuencía de numeros entre {} y {} es: {}\n'.format(inicio,fin,prom))


def ej2():
    print("\n\n     Ej2:Mi Calculadora (^_^)")

    '''
    Tome el ejercicio de clase:
    <condicionales_python /  ejercicios_practica / ej3>,
    copielo a este ejercicio y modifíquelo, ahora se deberá ejecutar
    indefinidamente hasta que como operador se ingrese la palabra "FIN",
    en ese momento debe terminar el programa

    Se debe debe imprimir un cartel de error si el operador ingresado no es
    alguno de lo soportados o no es la palabra "FIN"
    '''

    
    op_menu = 'inicia'  #inicialización de la opción menu
    op_num = 'N'        #inicialización de la opción número
    print("Ingrese dos números:")
    num_1 = float(input())
    num_2 = float(input())

    while op_menu != 'FIN' and op_menu != 'fin':
        print('''\nIngrese el simbolo de la operación que desee realizar:
        - Suma (+)
        - Resta (-)
        - Multiplicación (*)
        - División (/)
        - Exponente/Potencia (**)
        
        - FIN para salir''')
        op_menu = str(input())

        if (op_menu != '+' and op_menu != '-' and op_menu != '*' and op_menu != '/' 
        and op_menu != '**' and op_menu !='FIN' and op_menu !='fin'):
           print("ERROR! Ingrese una opción valida del menu")
           continue
        elif op_menu == '+':
            print("SUMA:\n{} + {} = {}".format(num_1,num_2,num_1+num_2))
        elif op_menu == '-':
            print("RESTA:\n{} - {} = {}".format(num_1,num_2,num_1-num_2))
        elif op_menu == '*':
            print("MULTIPLICACIÓN:\n{} x {} = {}".format(num_1,num_2,num_1*num_2))
        elif op_menu == '/':
            print("DIVISIÓN:\n{} : {} = {}".format(num_1,num_2,num_1/num_2))
        elif op_menu == '**':
            print("POTENCIA:\n{} ^ {} = {}".format(num_1,num_2,num_1**num_2))
       
        if op_menu != 'fin' and op_menu != 'FIN':
            op_num = str(input('¿Desea ingresar otro par de números? S/N   '))
            while (op_num != 's' and op_num != 'S' 
                and op_num != 'N' and op_num != 'n'):
                op_num = str(input('ERROR! Ingrese S/N   '))
            
            if op_num == 'S' or op_num == 's':
                print("Ingrese dos números:")
                num_1 = float(input())
                num_2 = float(input())


def ej3():
    print("\n\n     Ej3:Mi organizador académico (#_#)")

    '''
    Tome el ejercicio de "calificaciones":
    <condicionales_python / ejercicios_clase / ej3>,
    copielo a este ejercicio y modifíquelo para cumplir
    el siguiente requerimiento

    Las notas del estudinte se encuentran almacenadas en una
    lista llamada "notas" que ya hemos definido al comienzo del archivo

    Debe caluclar el promedio de todas las notas y luego transformar
    la califiación en una letra según la escala establecida en el ejercicio
    "calificaciones" <condicionales_python / ejercicios_clase / ej3>

    A medida que recorre las notas, no debe considerar como válidas aquellas
    que son negativas, en ese caso el alumno estuvo ausente

    Debe contar la cantidad de notas válidas y la cantidad de ausentes
    '''
    
        
    # Para calcular el promedio primero debe obtener la suma
    # de todas las notas, que irá almacenando en esta variable
    acum = 0           # Ya le hemos inicializado en 0

    cant_notas = 0      # Aquí debe contar cuantas notas válidas encontró
    cant_ausentes = 0   # Aquí debe contar cuantos ausentes hubo

    # Realice aquí el bucle para recorrer todas las notas
    # y cacular la sumatoria
    print('Notas del alumno:\n',notas)

    for i in range(len(notas)):
        if notas[i] >= 0:
            acum += notas[i]
            cant_notas += 1
        else:
            cant_ausentes += 1


    # Terminado el bucle calcule el promedio como
    # promedio = sumatoria / cantidad_notas

    nota_prom = acum/cant_notas

    print('Nota promedio del alumno:  ',nota_prom)

    # Utilice la nota promedio calculada y transformela
    # a calificación con letras, imprima en pantalla el resultado
    print('La calificación del alumno es:')
    
    if nota_prom >= 90:
        print("A")
    elif nota_prom >= 80:
        print("B")
    elif nota_prom >= 70:
        print("C")
    elif nota_prom >= 60:
        print("D")
    else:
        print("F")

    # Imprima en pantalla al cantidad de ausentes

    print('Ausente: ',cant_ausentes)


def ej4():
    print("\n\nMi primer pasito en data analytics")

    '''
    Tome el ejercicio:
    <condicionales_python / ejercicios_practica /ej5>,
    copielo a este ejercicio y modifíquelo para cumplir el
    siguiente requerimiento

    En este ejercicio se lo provee de una lista de temperatuas,
    esa lista de temperatuas corresponde a los valores de temperaturas
    tomados durante una temperorada del año en Buenos Aires.
    Ustede deberá analizar dicha lista para deducir
    en que temporada del año se realizó el muestreo de temperatura.
    La variable con la lista de temperaturas se llama "temp_dataloger"
    definida al comienzo del archivo

    Debe recorrer la lista "temp_dataloger" y obtener los siguientes
    resultados

    1 - Obtener la máxima temperatura
    2 - Obtener la mínima temperatura
    3 - Obtener el promedio de las temperatuas

    Los resultados se deberán almacenar en las siguientes variables
    que ya hemos preparado para usted.
    
    NOTA: No se debe ordenar la lista de temperaturas, se debe obtener
    el máximo y el mínimo utilizando los mismos métodos vistos
    durante la clase (ejemplos_clase)
    '''

    print('\n     Ej4:Mediciones de temperatura en Bs As')
    print('Temperaturas [ºC]: ',temp_dataloger)

    temperatura_max = None     # Aquí debe ir almacenando la temp máxima
    temperatura_min = None      # Aquí debe ir almacenando la temp mínima
    temperatura_sumatoria = 0   # Aquí debe ir almacenando la suma de todas las temp
    temperatura_promedio = 0    # Al finalizar el loop deberá aquí alamcenar el promedio
    temperatura_len = 0         # Aquí debe almacenar cuantas temperatuas hay en la lista

    # Colocar el bucle aqui......

    for i in range(len(temp_dataloger)):
        if (temperatura_max is None) or (temp_dataloger[i] > temperatura_max):
            temperatura_max = temp_dataloger[i]
        if (temperatura_min is None) or (temp_dataloger[i] < temperatura_min):
            temperatura_min = temp_dataloger[i]
        temperatura_sumatoria += temp_dataloger[i]
        temperatura_len += 1
    
    print('Temperatura máx: {}ºC'.format(temperatura_max))
    print('Temperatura min: {}ºC'.format(temperatura_min))
    

    # Al finalizar el bucle compare si el valor que usted calculó para
    # temperatura_max y temperatura_min coincide con el que podría calcular
    # usando la función "max" y la función "min" de python
    # función "max" --> https://www.w3schools.com/python/ref_func_max.asp
    # función "min" --> https://www.w3schools.com/python/ref_func_min.asp

    print('Temperatura máxima con funciones de python: {}ºC'.format(max(temp_dataloger)))
    print('Temperatura minima con funciones de python: {}ºC'.format(min(temp_dataloger)))


    # Al finalizar el bucle debe calcular el promedio como:
    temperatura_promedio = temperatura_sumatoria / temperatura_len

    print('\nLa temperatura promedio de la temporada fue de: {}ºC'.format(temperatura_promedio))

    # Corroboren los resultados de temperatura_sumatoria
    # usando la función "sum"
    # función "sum" --> https://www.w3schools.com/python/ref_func_sum.asp

    print('\nSumatoria de temperatura: {}ºC'.format(temperatura_sumatoria))
    print('Sumatoria de temperatura con funciones de python: {}ºC'.format(sum(temp_dataloger)))

    '''
    Una vez que tengamos nuestros valores correctamente calculados debemos
    determinar en que epoca del año nos encontramos en Buenos Aires utilizando
    la estadística de años anteriores. Basados en el siguiente link realizamos
    las siguientes aproximaciones:

    verano -->      min = 19, max = 28
    otoño -->       min = 11, max = 24
    invierno -->    min = 8, max = 14
    primavera -->   min = 10, max = 24

    Referencia:
    https://es.weatherspark.com/y/28981/Clima-promedio-en-Buenos-Aires-Argentina-durante-todo-el-a%C3%B1o
    '''

    # En base a los rangos de temperatura de cada estación,
    # ¿En qué época del año nos encontramos?
    # Imprima el resultado en pantalla
    # Debe utilizar temperatura_max y temperatura_min para definirlo

    print('\nSegún los datos de la lista se midieron en la temporada de: ')

    if temperatura_min > 19  and temperatura_max < 28:
        print('VERANO')
    elif temperatura_min > 11 and temperatura_max < 24:
        print('OTOÑO')
    elif temperatura_min > 10 and temperatura_max < 24:
        print('PRIMAVERA')
    elif temperatura_min > 8 and temperatura_max < 14:
        print('INVIERNO')


def ej5():
    print("\nAhora sí! buena suerte :)")

    '''
    Tome el ejercicio:
    <condicionales_python / ejercicios_practica / ej4>,
    copielo a este ejercicio y modifíquelo para cumplir
    el siguiente requerimiento

    Realize un programa que corra indefinidamente en un bucle, al comienzo de la
    iteración del bucle el programa consultará al usuario con el siguiente menú:
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)
    3 - Salir del programa

    En caso de presionar "3" el programa debe terminar e informar por
    pantalla de que ha acabado,
    en caso contrario si se presionar "1" o "2" debe continuar con la siguiente tarea

    NOTA: Si se ingresa otro valor que no sea 1, 2 o 3 se debe enviar
    un mensaje de error y volver a comenzar el bucle
    (vea en el apunte "Bucles - Sentencias" para encontrar
    la sentencia que lo ayude a cumplir esa tarea)

    Si el bucle continua (se presionó "1" o "2") se debe ingresar a otro bucle
    en donde en cada iteración se pedirá una palabra. La cantidad de iteración
    (cantidad de palabras a solicitar) lo dejamos a gusto del alumno, intente que esa
    condición esté dada por una variable (ej: palabras_deseadas = 4)
    Cada palabra ingresada se debe ir almacenando en una lista de palabras, dicha
    lista la debe inicializar vacia y agregar cada nuevo valor con el método "append".
    Luego de tener las palabras deseadas almacenadas en una lista de palabras
    se debe proceder a realizar las siguientes tareas:

    Si se ingresa "1" por consola se debe obtener la palabra
    más grande por orden alfabético
    Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
    se debe imprimir en pantalla cual era la palabra
    más grande alfabeticamente.
    Recuerde que debe inicializar primero su variable
    donde irá almacenando la palabra que cumpla dicha condición.
    ¿Con qué valor debería ser inicializada dicha variable?

    Si se ingresa "2" por consola se debe obtener la palabra
    con mayor cantidad de letras
    Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
    se debe imprimir en pantalla cual era la palabra con
    mayor cantidad de letras.
    Recuerde que debe inicializar primero su variable
    donde irá almacenando la palabra que cumpla dicha condición.
    ¿Con qué valor debería ser inicializada dicha variable?
    
    NOTA: No se debe ordenar la lista de palabras, se debe obtener
    el máximo utilizando el mismos métodos vistos durante la clase
    (ejemplos_clase), tal como el ejercicio anterior. Ordenar una
    lista representa un problema mucho más complejo que solo
    buscar el máximo.

    NOTA: Es recomendable que se organice con lápiz y papel para
    hacer un bosquejo del sistema ya que deberá utilizar 3 bucles en total,
    1 - El bucle principal que hace que el programa corra hasta ingresar un "3"
    2 - Un bucle interno que corre hasta socilitar todas las palabras deseadas
        que se deben ir guardando en una lista
    3- Otro bucle interno que corre luego de que termine el bucle "2" que
       recorre la lista de palabras y busca la mayor según el motivo ingresado ("1" o "2")

    '''
    print("\n\n     Ej5:Orden de palabras")
    print('Ingrese la tarea que desee realizar del menu')  
    palabras = []

    while True:
        palabras.clear()
        print('''            
                    MENU
        1 - Ordenar por orden alfabético 
        2 - Ordenar por cantidad de letras 
        3 - Salir del programa\n''')

        opc = str(input('Ingrese el número opcion deseada:  '))

        if opc != '1' and opc != '2' and opc !='3':
            print('la opción es incorrecta, por favor ingrese una opción valida al menu que se detalla')
            continue
        elif opc == '3':
            print('FIN DEL PROGRAMA, ADÍOS!!')
            break

        cant_pal = int(input('\nIngrese la cantidad de palabras con las que desea trabajar:  '))

        for i in range(cant_pal):
            palabras.append(str(input('Ingerese {}º palabra\n'.format(i+1))))
        if opc == '1':
            print('\nEl orden alfabetico de las palabras ingresadas es:')

            for i in range(len(palabras)):
                for t in range(len(palabras)):
                    if palabras[t] < palabras[i]:
                        aux = palabras[i]
                        palabras[i] = palabras[t]
                        palabras[t] = aux
            print(palabras)
            continue
        
        else:
            print('\nEl orden de las palabras segun la cantidad de letras es:')
            for i in range(len(palabras)):
                for t in range(len(palabras)):
                    if len(palabras[t]) < len(palabras[i]):
                        aux = palabras[i]
                        palabras[i] = palabras[t]
                        palabras[t] = aux
            print(palabras)
            continue




    

  


if __name__ == '__main__':
    print("\n                   Ejercicios de práctica\n")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
    print("\n\n********************* FIN DE EJERCICOS *********************")
