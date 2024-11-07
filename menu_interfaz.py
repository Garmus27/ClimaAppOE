from clima_API import obtener_clima
from Settings import cambiar_unidades, obtener_unidades
from errores import ValidationError, APIError

def mostrar_menu():
    while True:
        print("\nMenú:")
        print("1. Consultar clima")
        print("2. Configuración")
        print("3. Ver consultas guardadas")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            try:
                ciudad = input("Ingrese el nombre de la ciudad: ")
                if not ciudad.isalpha():
                    raise ValidationError(message=f"Nombre de ciudad no válido: {ciudad}")
                clima = obtener_clima(ciudad)
                if clima.get("error"):
                    print(f"Error al obtener el clima: {clima['error']}")
                else:
                    mostrar_clima_formateado(clima)
            except ValidationError as e:
                print(e)
            except APIError as e:
                print(e)
        elif opcion == '2':
            mostrar_configuracion()
        elif opcion == '3':
            mostrar_consultas_guardadas()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

def mostrar_clima_formateado(clima):
    print(f"\nClima actual en {clima['ciudad']}:")
    print(f"Temperatura: {clima['temperatura']}")
    print(f"Presion: {clima['presion']}")
    print(f"Humedad: {clima['humedad']}")
    print(f"Descripcion: {clima['descripcion']}")

def mostrar_configuracion():
    while True:
        print("\nConfiguración:")
        print("1. Cambiar unidades de medida")
        print("2. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            print("\nOpciones de unidades de medida:")
            print("1. Celsius")
            print("2. Fahrenheit")
            print("3. Kelvin")
            
            unidad = input("Seleccione una unidad (1/2/3): ")
            
            if unidad == '1':
                cambiar_unidades("metric")
            elif unidad == '2':
                cambiar_unidades("imperial")
            elif unidad == '3':
                cambiar_unidades("standard")
            else:
                print("Opción no válida. Se configurarán las unidades en Celsius por defecto.")
                cambiar_unidades("metric")
            
            print(f"Unidades de medida establecidas a: {obtener_unidades()}")
        elif opcion == '2':
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

def mostrar_consultas_guardadas():
    try:
        with open("consultas_clima.txt", "r") as file:
            print("\nConsultas guardadas:")
            consultas = file.readlines()
            for consulta in consultas:
                print(consulta, end='')
    except FileNotFoundError:
        print("No hay consultas guardadas.")




