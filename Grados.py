'''
Jorge Maldonado
Programa 1: Temperaturas
Crea un programa en Python que convierta temperaturas entre Fahrenheit y Celsius para múltiples entradas. 

El programa debe:

    Preguntar al usuario cuántas temperaturas desea convertir.
    Usar un bucle para solicitar al usuario cada temperatura y su unidad (F o C).
    Almacenar las temperaturas de entrada y sus unidades en listas separadas.
    Convertir todas las temperaturas a la unidad opuesta.
    Mostrar las temperaturas originales y convertidas en formato tabular.

Requisitos:

    Utiliza listas para almacenar las temperaturas de entrada, unidades y temperaturas convertidas.
    Implementa un bucle para recopilar múltiples entradas de temperatura.
    Usa comprensión de listas para realizar las conversiones.
    Formatea la salida como una tabla con columnas alineadas.
    hh

'''
# Funciones
def fahrenheit_a_celsius(f):
    return (f - 32) * 5 / 9

def celsius_a_fahrenheit(c):
    return (c * 9 / 5) + 32

# Función principal
def main():
    # Solicitar al usuario cuantas temperaturas desea convertir
    n = int(input("¿Cuántas temperaturas desea convertir? "))
    
    # Inicializar listas para almacenar temperaturas y unidades
    temperaturas = []
    unidades = []
    
    # Bucle para solicitar las temperaturas y sus unidades
    for i in range(n):
        temp = float(input(f"Ingrese la temperatura #{i + 1}: "))
        unidad = input("Ingrese la unidad (F para Fahrenheit, C para Celsius): ").upper()
        
        # Validar la unidad ingresada
        while unidad not in ['F', 'C']:
            print("Unidad no válida. Por favor ingrese 'F' o 'C'.")
            unidad = input("Ingrese la unidad (F para Fahrenheit, C para Celsius): ").upper()
        
        # Almacenar la temperatura y su unidad en las listas
        temperaturas.append(temp)
        unidades.append(unidad)
    
    # Convertir las temperaturas a la unidad opuesta
    temperaturas_convertidas = [
        fahrenheit_a_celsius(temp) if unidad == 'F' else celsius_a_fahrenheit(temp)
        for temp, unidad in zip(temperaturas, unidades)
    ]
    
    # Mostrar las temperaturas originales y convertidas en formato tabular
    print("\nTemperaturas originales y convertidas:")
    print(f"{'Temperatura Original':<20} {'Unidad':<10} {'Temperatura Convertida':<25} {'Unidad Convertida'}")
    for temp, unidad, temp_conv in zip(temperaturas, unidades, temperaturas_convertidas):
        if unidad == 'F':
            print(f"{temp:<20} {unidad:<10} {temp_conv:<25.2f} {'C'}")
        else:
            print(f"{temp:<20} {unidad:<10} {temp_conv:<25.2f} {'F'}")

# Ejecutar la función principal
if __name__ == "__main__":
    main()