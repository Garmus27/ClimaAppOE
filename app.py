import datetime
from datetime import timedelta


def guardar_en_historial(consulta):
    historial = cargar_historial()
    fecha_actual = datetime.datetime.now().isoformat()
    historial.append({"fecha": fecha_actual, "consulta": consulta})

def filtrar_historial(dias):
    historial = cargar_historial()
    limite = datetime.datetime.now() - timedelta(days=dias)
    return [item for item in historial if datetime.datetime.fromisoformat(item["fecha"]) >= limite]

# Función para obtener próximos 5 días
def obtener_clima(ciudad):
    api_key = "TU_API_KEY_AQUI"  # Reemplazar con API Key
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={ciudad}&appid={api_key}&units=metric&cnt=5"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        datos_clima = respuesta.json()
        pronostico = []
        for item in datos_clima['list']:
            fecha = item['dt_txt']
            temperatura = item['main']['temp']
            descripcion = item['weather'][0]['description']
            pronostico.append(f"Fecha: {fecha}, Temp: {temperatura}°C, Descripción: {descripcion}")
        return pronostico
    else:
        return f"Error obteniendo el clima: {respuesta.status_code}"

# Menú
print("=== Menú Historial ===")
print("1. Ver últimos 15 días")
print("2. Ver últimos 30 días")
print("3. Ver clima próximos 5 días")
print("4. Salir")
opcion = input("Elige una opción: ")

if opcion == "1":
    resultados = filtrar_historial(15)
    print(resultados)
elif opcion == "2":
    resultados = filtrar_historial(30)
    print(resultados)
elif opcion == "3":
    ciudad = input("Ingresa la ciudad para el pronóstico del clima: ")
    clima = obtener_clima(ciudad)
    print(clima)
elif opcion == "4":
    print("Saliendo del programa...")
else:
    print("Opción no válida. Intenta nuevamente.")

