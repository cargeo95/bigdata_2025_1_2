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
    
    

if __name__ == "__main__":
    main()
