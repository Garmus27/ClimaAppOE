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