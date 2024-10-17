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