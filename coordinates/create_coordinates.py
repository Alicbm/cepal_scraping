from geopy.geocoders import Nominatim
import pandas as pd

df = pd.read_excel("/mnt/c/Users/Alic Barandica/Documents/proyectos/cepal_scraping/files/demografia/Población total, según sexo.xlsx")

countries = df['País__ESTANDAR'].unique()
# print(countries)

geolocator = Nominatim(user_agent="geoapi_exercises")

def obtener_coordenadas(pais):
    location = geolocator.geocode(pais)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

datos = []
for pais in countries:
    try:
      new_pais = pais[:38]
      latitud, longitud = obtener_coordenadas(new_pais)
      datos.append({"País": pais, "Latitud": latitud, "Longitud": longitud})
    except Exception as e:
      print(f"Error obteniendo las coordenadas de {pais}: {e}")

df = pd.DataFrame(datos)

df.to_excel('/mnt/c/Users/Alic Barandica/Documents/proyectos/cepal_scraping/coordinates/countries_coodinates.xlsx', index=False)

#con problemas de internet se corta, pero sigue intentando

