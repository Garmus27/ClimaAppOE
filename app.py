import requests

api_key = "ff665520476ccad9dc27238103288d2c"

base_url = "https://api.openweathermap.org/data/2.5/weather?"

city_name = input("ingrese una ciuedad")

url = base_url + "q=" + city_name + "&appid=" + api_key

response = requests.get(url)

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
    print("Ciudad no encontrada.")

