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
    print(nombre_tabla)
    database.insert_data(dw.df, nombre_tabla)
    print(database)
    df_2 = database.read_data(nombre_tabla)
    print(df_2.head())
    
    print("DataFrame a insertar:")
    print(dw.df.head())
    print("Shape del DataFrame:", dw.df.shape)
    

if __name__ == "__main__":
    main()
