'''
Programa 2: Manipulación de Listas

Crea un programa en Python que realice varias operaciones en una lista de números.

El programa debe:

    Pedir al usuario que ingrese una serie de números, separados por espacios.
    Convertir la entrada en una lista de enteros.
    Realizar las siguientes operaciones y mostrar los resultados:
        Calcular la suma de todos los números. 
        Encontrar los valores máximo y mínimo.
        Calcular el promedio (media) de los números.
        Eliminar cualquier número duplicado y mostrar la lista actualizada.
        Ordenar la lista en orden ascendente.
        Crear una nueva lista que contenga solo los números pares de la lista original.

Requisitos:
    Utiliza métodos de lista y funciones incorporadas para realizar las operaciones.
    Implementa comprensión de listas para crear la lista de números pares.
    Usa un conjunto (set) para eliminar duplicados.
    Formatea la salida de manera clara, mostrando el resultado de cada operación.
    '''

# Programa 2: Manipulación de Listas

def main():
    # Pedir al usuario que ingrese números separados por espacios
    entrada = input("Ingrese una serie de números separados por espacios: ")
    
    # Convertir la entrada en una lista de enteros
    numeros = [int(num) for num in entrada.split()]
    
    print("\n--- Resultados ---")
    
    # 1. Calcular la suma de todos los números
    suma = sum(numeros)
    print(f"\n1. Suma total: {suma}")
    
    # 2. Encontrar valores máximo y mínimo
    maximo = max(numeros)
    minimo = min(numeros)
    print(f"2. Valor máximo: {maximo}")
    print(f"   Valor mínimo: {minimo}")
    
    # 3. Calcular el promedio (media)
    promedio = suma / len(numeros)
    print(f"3. Promedio: {promedio:.2f}")
    
    # 4. Eliminar duplicados y mostrar lista actualizada
    numeros_sin_duplicados = list(set(numeros))
    print(f"4. Lista sin duplicados: {numeros_sin_duplicados}")
    
    # 5. Ordenar la lista en orden ascendente
    numeros_ordenados = sorted(numeros_sin_duplicados)
    print(f"5. Lista ordenada: {numeros_ordenados}")
    
    # 6. Crear lista con solo números pares (usando comprensión de listas)
    numeros_pares = [num for num in numeros if num % 2 == 0]
    print(f"6. Números pares: {numeros_pares}")

if __name__ == "__main__":
    main()