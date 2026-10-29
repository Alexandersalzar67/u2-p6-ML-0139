import pandas as pd
import numpy as np

serie_amigos=["abi","pau","yuritzi","gisele","aylin","jade","cristopher"]
print("serie de listado de amigos nc = 0139")
amigos=pd.Series(serie_amigos)
print(amigos)

serie_billetes=[20,50,100,200,500,1000]
print("serie de listado valor de billetes nc = 0139")
amigos=pd.Series(serie_billetes)
print(amigos)

serie_billetes=[20,50,100,200,500,1000]
serie_billetras=["veinte","cincuenta","cien","docientos","quinientos","mil"]
print("serie de listado nombre y valor de billetes MX nc = 0139")
tablabilletes=pd.Series(serie_billetes, serie_billetras)
print(tablabilletes)
# dicionario data frame
# diccionario de valor monedas y monedas
print("datos de diccionario a data frame en pandas")
dic_monedas={
    "series_monedas" : [20,50,100,200,500,1000],
    "serie_billetras" :["veinte","cincuenta","cien","docientos","quinientos","mil"]
}

TablaAlex=pd.DataFrame(dic_monedas,index=["A","B","C","D","E","F"])
print(tablabilletes)
print("CASA DE CAMBIO ALEXANDER SALAZAR 0139")