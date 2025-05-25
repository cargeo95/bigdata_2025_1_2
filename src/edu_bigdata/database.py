import os
import datetime
import sqlite3
import pandas as pd

class DataBase:
    def __init__(self):
        self.db_name = "src/edu_bigdata/static/db/minas_analisis.sqlite"

     
    # def create_database(self):
    #     try:
    #         self.conn = sqlite3.connect(self.db_name)
    #         self.cursor = self.conn.cursor()
    #         self.conn.close()
            
    #     except Exception as err:
    #         print("Error al crear la base de datos")
    #         # df.sql(self.conn, nom_tabla)
    
    #CRUD  
    def insert_data(self, df=pd.DataFrame(), nom_table="minas_analisis"):
        try:
            df = df.copy()
            
            # Convertir columnas de objetos/dict a string si es necesario
            if 'geocoded_column' in df.columns:
                df['geocoded_column'] = df['geocoded_column'].apply(str)

            print("Insertando datos a la base de datos:")
            print(df.head())
            print("Shape:", df.shape)
            print("Dtypes:", df.dtypes)

            conn = sqlite3.connect(self.db_name)
            df.to_sql(name=nom_table, con=conn, if_exists='replace', index=False)
            conn.close()
            print("Datos insertados correctamente.")
        except Exception as errores:
            print("Error al guardar los datos:", errores)
    
    def read_data(self,nom_table=""):
        df=pd.DataFrame()
        try:
            if len(nom_table)>0:
                conn = sqlite3.connect(self.db_name)
                query= "select * from {}".format(nom_table)
                df = pd.read_sql_query(sql=query,con=conn)
                print("*************** consulta base datos tabla: {}*********".format(query))
                conn.close()
                return df
        except Exception as errores:
            print("error al obtener los datos")
            return df
    
