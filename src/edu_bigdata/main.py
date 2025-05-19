from dataweb import DataWeb
import pandas as pd

def main():
    dw = DataWeb()
    dw.obtener_datos()
    dw.crear_dataframe()
    dw.convertir_numericos()
    dw.exportar_csv()

    dw.df.to_csv("src/edu_bigdata/static/csv/data_web.csv", index=False)

if __name__ == "__main__":
    main()
