import random
import time

#  Algoritmo 1: Bubble Sort 
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

#  Algoritmo 2: Merge Sort 
def merge_sort(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]

        merge_sort(izquierda)
        merge_sort(derecha)

        i = j = k = 0
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

#  Algoritmo 3: Quick Sort 
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x < pivote]
        mayores = [x for x in lista[1:] if x >= pivote]
        return quick_sort(menores) + [pivote] + quick_sort(mayores)

#  Función para medir el tiempo que tarda cada algoritmo 
def medir_tiempo(algoritmo, lista):
    inicio = time.time()
    algoritmo(lista)  
    fin = time.time()
    return fin - inicio

#  Menú principal 
def menu():
    while True:
        print("\n--- Comparador de Algoritmos de Ordenamiento ---")
        print("1. Ordenar lista con Bubble Sort")
        print("2. Ordenar lista con Merge Sort")
        print("3. Ordenar lista con Quick Sort")
        print("4. Comparar los tres algoritmos")
        print("5. Salir")
        opcion = input("Elegí una opción (1-5): ")

        if opcion in ["1", "2", "3", "4"]:
            try:
                tamaño = int(input("¿Cuántos números aleatorios querés generar? "))
                lista_original = [random.randint(1, 10000) for _ in range(tamaño)]
            except:
                print("Ingresaste un valor no válido.")
                continue

        if opcion == "1":
            lista = lista_original.copy()
            t = medir_tiempo(bubble_sort, lista)
            print("Bubble Sort completado.")
            print(f"Tiempo: {t:.6f} segundos.")

        elif opcion == "2":
            lista = lista_original.copy()
            t = medir_tiempo(merge_sort, lista)
            print("Merge Sort completado.")
            print(f"Tiempo: {t:.6f} segundos.")

        elif opcion == "3":
            lista = lista_original.copy()
            t = medir_tiempo(quick_sort, lista)
            print("Quick Sort completado.")
            print(f"Tiempo: {t:.6f} segundos.")

        elif opcion == "4":
            for alg in [bubble_sort, merge_sort, quick_sort]:
                lista = lista_original.copy()
                t = medir_tiempo(alg, lista)
                print(f"{alg.__name__} → {t:.6f} segundos.")

        elif opcion == "5":
            print("¡Gracias por usar el comparador!")
            break 

        else:
            print("Opción no válida. Por favor, elegí entre 1 y 5.")

#  Ejecutar el menú 
menu()
