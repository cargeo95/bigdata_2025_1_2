from dataweb import DataWeb
from database import DataBase
import pandas as pd

def main():
    dw = DataWeb()
    database = DataBase()
    dw.obtener_datos()
    dw.crear_dataframe()
    dw.convertir_numericos()
    dw.exportar_csv()
    dw.df.to_csv("src/edu_bigdata/static/csv/data_web.csv", index=False)
    nombre_tabla = "minas_analisis"
    database.insert_data(dw,nombre_tabla)
    df_2 = database.read_data(nombre_tabla)
    print(df_2.head())
    

if __name__ == "__main__":
    main()
