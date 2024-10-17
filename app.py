class Settings:
    def __init__(self):
        self.unidad_temperatura = "Celsius"  # Unidad por defecto

    def cambiar_unidad_temperatura(self):
        print("Unidades de Temperatura:")
        print("1. Celsius")
        print("2. Fahrenheit")
        opcion = input("Elige la unidad (1 o 2): ")

        if opcion == "1":
            self.unidad_temperatura = "Celsius"
        elif opcion == "2":
            self.unidad_temperatura = "Fahrenheit"
        else:
            print("Opción no válida. Se mantiene la unidad actual.")

        print(f"Unidad de temperatura actual: {self.unidad_temperatura}")

    def configuracion_actual(self):
        print("Configuraciones actuales:")
        print(f"Temperatura: {self.unidad_temperatura}")


def settings_menu():
    settings = Settings()

    while True:
        print("--- Menú de Configuración ---")
        print("1. Cambiar unidad de temperatura")
        print("2. Mostrar configuracion actual")
        print("3. Salir")

        eleccion = input("Elige una opción (1-3): ")

        if eleccion == "1":
            settings.cambiar_unidad_temperatura()
        elif eleccion == "2":
            settings.configuracion_actual()
        elif eleccion == "3":
            print("Saliendo del menú de configuración.")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


# Ejecución de la aplicación
settings_menu()

import requests

api_key = "ff665520476ccad9dc27238103288d2c"

base_url = "https://api.openweathermap.org/data/2.5/weather?"

city_name = input("Ingrese una ciudad: ")

url = base_url + "q=" + city_name + "&appid=" + api_key

try:
    response = requests.get(url)
    response.raise_for_status()  # Esto genera un error para códigos de estado HTTP 4xx o 5xx

    data = response.json()

    if data["cod"] != "404":
        # Extraer el bloque principal de información
        main = data["main"]
        # Extraer la temperatura
        temperatura = main["temp"]
        # Extraer la presión
        presion = main["pressure"]
        # Extraer la humedad
        humedad = main["humidity"]
        
        # Extraer la descripción del clima
        descripcion = data["weather"][0]["description"]
        
        # Imprimir los resultados
        print(f"Temperatura: {temperatura} K")
        print(f"Presión: {presion} hPa")
        print(f"Humedad: {humedad}%")
        print(f"Descripción del clima: {descripcion}")
    else:
        print({"codigo_error": 404, "mensaje": "Ciudad no encontrada."})

except requests.exceptions.ConnectionError:
    print({"codigo_error": 100, "mensaje": "Error de conexión. Verifique su conexión a Internet."})

except requests.exceptions.Timeout:
    print({"codigo_error": 101, "mensaje": "La solicitud excedió el tiempo de espera."})

except requests.exceptions.RequestException as e:
    # Cualquier otro tipo de error relacionado con la solicitud
    print({"codigo_error": 102, "mensaje": f"Error al realizar la solicitud: {str(e)}"})
