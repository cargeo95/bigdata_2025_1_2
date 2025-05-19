import pandas as pd
import requests

class DataWeb:
    def __init__(self, url="https://www.datos.gov.co/resource/sgp4-3e6k.json"):
        self.url = url
        self.data = None
        self.df = None

    def obtener_datos(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.data = response.json()
            print("Datos obtenidos correctamente.")
        else:
            raise Exception(f"Error al obtener datos: {response.status_code}")

    def crear_dataframe(self):
        if self.data is not None:
            self.df = pd.DataFrame(self.data)
            print("DataFrame creado con éxito.")
        else:
            raise ValueError("Los datos no han sido descargados. Llama primero a obtener_datos().")

    def convertir_numericos(self):
        if self.df is not None:
            self.df = self.df.apply(pd.to_numeric, errors='ignore')
            print("Conversión a valores numéricos completada.")
        else:
            raise ValueError("El DataFrame no ha sido creado.")

    def exportar_csv(self, nombre_archivo="data_web.csv"):
        if self.df is not None:
            self.df.to_csv(nombre_archivo, index=False, encoding='utf-8')
            print(f"Archivo exportado como {nombre_archivo}")
        else:
            raise ValueError("El DataFrame no ha sido creado.")
