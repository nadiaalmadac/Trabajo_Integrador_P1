import os #Libreria recomendada para la funcion decorativa limpiar pantalla

#Funcion de Limpiar pantalla
def limpiar_pantalla():
    # Detecta el sistema operativo
    if os.name == 'nt':
        # Windows
        os.system('cls')
    else:
        # Unix/Linux/Mac
        os.system('clear')

def imprimir_arbol_grafico(arbol, nivel=0):
    # Función para imprimir el árbol con formato gráfico usando indentación
    if arbol == []:
        # Si el árbol está vacío, no hacemos nada y salimos
        return
    # Primero imprimir el hijo derecho (se imprime arriba en el gráfico)
    imprimir_arbol_grafico(arbol[2], nivel + 1)
    # Imprimir el nodo actual con indentación proporcional al nivel
    print("    " * nivel + str(arbol[0]))
    # Finalmente imprimir el hijo izquierdo (se imprime abajo en el gráfico)
    imprimir_arbol_grafico(arbol[1], nivel + 1)

def construir_arbol(arbol):
    pendientes = []  # Lista para guardar nodos que aún pueden tener hijos (pendientes de completar)

    while True:
        limpiar_pantalla()
        # Si el árbol está vacío, avisamos que el próximo valor será la raíz
        if arbol == []:
            print("El árbol está vacío. Ingrese el valor para la raíz.")
        else:
            # Si no está vacío, buscamos el primer nodo con espacio para insertar un hijo
            for nodo in pendientes:
                if nodo[1] == []:  # Si el hijo izquierdo está vacío
                    print(f"El próximo valor se agregará como hijo izquierdo de '{nodo[0]}'")
                    break  # Salimos del ciclo porque ya sabemos dónde insertar
                elif nodo[2] == []:  # Si el hijo derecho está vacío
                    print(f"El próximo valor se agregará como hijo derecho de '{nodo[0]}'")
                    break  # Salimos del ciclo porque ya sabemos dónde insertar

        # Pedimos al usuario que ingrese un valor o escriba 'salir' para terminar
        valor = input("Ingresá un valor para el árbol (o escribí 'salir' para terminar): ")
        if valor.lower() == 'salir':
            # Si el usuario escribe 'salir', rompemos el ciclo y terminamos la función
            break

        # Si el árbol está vacío, creamos la raíz con el valor ingresado
        if arbol == []:
            arbol += [valor, [], []]  # Creamos el nodo raíz con [valor, hijo_izquierdo, hijo_derecho]
            pendientes.append(arbol)   # Agregamos la raíz a la lista de nodos pendientes
            print(f"Raíz creada con el valor '{valor}'")
            continue  # Volvemos a pedir el próximo valor

        # Si el árbol no está vacío, buscamos dónde insertar el nuevo valor
        for nodo in pendientes:
            if nodo[1] == []:  # Si el hijo izquierdo está vacío
                nodo[1] = [valor, [], []]  # Insertamos el nuevo nodo como hijo izquierdo
                pendientes.append(nodo[1])  # Añadimos el nuevo nodo a pendientes para futuros hijos
                print(f"'{valor}' agregado como hijo izquierdo de '{nodo[0]}'")
                break  # Salimos del ciclo para pedir el siguiente valor
            elif nodo[2] == []:  # Si el hijo derecho está vacío
                nodo[2] = [valor, [], []]  # Insertamos el nuevo nodo como hijo derecho
                pendientes.append(nodo[2])  # Añadimos el nuevo nodo a pendientes para futuros hijos
                print(f"'{valor}' agregado como hijo derecho de '{nodo[0]}'")
                break  # Salimos del ciclo para pedir el siguiente valor

    # Una vez terminado el ingreso de datos, imprimimos el árbol de forma gráfica
    limpiar_pantalla()
    print("Asi quedo el Arbol Binario:")
    imprimir_arbol_grafico(arbol)
    input("\nPresiona Enter para continuar...")

def inorden(arbol):
    # Función para imprimir el árbol en recorrido inorden: izquierda → nodo → derecha
    if arbol == []:
        # Si el árbol está vacío, no hacemos nada
        return
    inorden(arbol[1])        # Recorrer hijo izquierdo (llamada recursiva)
    print(arbol[0], end=", ") # Imprimir valor del nodo actual (en línea)
    inorden(arbol[2])        # Recorrer hijo derecho (llamada recursiva)

def preorden(arbol):
    # Función para imprimir el árbol en recorrido preorden: nodo → izquierda → derecha
    if arbol == []:
        return
    print(arbol[0], end=", ")  # Imprimir nodo actual
    preorden(arbol[1])         # Recorrer hijo izquierdo
    preorden(arbol[2])         # Recorrer hijo derecho

def postorden(arbol):
    # Función para imprimir el árbol en recorrido postorden: izquierda → derecha → nodo
    if arbol == []:
        return
    postorden(arbol[1])        # Recorrer hijo izquierdo
    postorden(arbol[2])        # Recorrer hijo derecho
    print(arbol[0], end=", ")  # Imprimir nodo actual

def menu():
    arbol = []  # Lista que representa el árbol, comienza vacía
    while True:
        limpiar_pantalla()
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Agregar valor al árbol")
        print("2. Imprimir árbol (Inorden)")
        print("3. Imprimir árbol (Preorden)")
        print("4. Imprimir árbol (Postorden)")
        print("5. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == '1':
            # Opción para agregar valores al árbol
            construir_arbol(arbol)
        elif opcion == '2':
            imprimir_arbol_grafico
            # Imprimir árbol usando recorrido inorden
            inorden(arbol)
            input("\nPresiona Enter para continuar...")
        elif opcion == '3':
            # Imprimir árbol usando recorrido preorden
            preorden(arbol)
            input("\nPresiona Enter para continuar...")
        elif opcion == '4':
            # Imprimir árbol usando recorrido postorden
            postorden(arbol)
            input("\nPresiona Enter para continuar...")
        elif opcion == '5':
            # Salir del programa
            break
        else:
            # Opción inválida ingresada por el usuario
            print("Opción inválida.")
            input("\nPresiona Enter para continuar...")

# Ejecutar el menú para empezar el programa
menu()