import pandas as pd
import matplotlib as plt
from helpers.crearBarras import graficasBarrasSantaFe
from helpers.crearTablas import crearTabla
from helpers.crearTablas import crearTablaSantaFe
from helpers.crearBarras import graficarBarras
from helpers.crearTorta import graficarTorta

tablaSiembra = pd.read_csv("./data/Siembras.csv")

siembraTotal = tablaSiembra.query("Arboles > 0")

siembraMedellin = tablaSiembra.query("Ciudad == 'Medellín'")


##FILTRO UNO SANTAFE DE ANTIOQUIA###


tablaSiembraSantafe = pd.read_csv("./data/Siembras.csv")

# print(tablaSiembraSantafe)
datosSiembra = tablaSiembraSantafe.query('Ciudad == "Santa Fe de Antioquia" and Arboles > 250')

datos = datosSiembra[['Ciudad','Arboles']]
print(datos)

#Aqui pintamos la tabala
crearTablaSantaFe(datos,"tabla")

#Aqui pintamos la grafica

graficasBarrasSantaFe(datos,'Ciudad','Arboles','tabla')



##FILTRO TRES BELMIRA###

tablaSiembraBelmira = pd.read_csv("./data/Siembras.csv")

# print(tablaSiembraSantafe)
datosSiembraBe = tablaSiembraBelmira.query('Vereda == "Rio Arriba" and Arboles>0')
datosSiembraBe2 = tablaSiembraBelmira.query('Vereda == "La Salazar" and Arboles>0')

datosBelmira = datosSiembraBe[['Vereda','Arboles']]
datosBelmira2 = datosSiembraBe2[['Vereda','Arboles']]
print(datosBelmira)
print('\n')
print(datosBelmira2)
print('\n')

crearTabla(datosBelmira,"tablaBelmira1")
crearTabla(datosBelmira2,"tablaBelmira2")


##FILTRO CINCO CARAMANTA###

tablaSiembraCaramanta = pd.read_csv("./data/Siembras.csv")

datosSiembraCaramanta = tablaSiembraCaramanta.query('Arboles>100')

datosCara = datosSiembraCaramanta[['Arboles']]

print(datosCara)
print('\n')

crearTabla(datosCara,"tablaCaramanta")



##FILTRO SEIX YARUMAL###

tablaSiembraYarumal = pd.read_csv("./data/Siembras.csv")

datosSiembraYarumal = tablaSiembraYarumal.query('Vereda == "Mallarino" and Arboles>0')

datosYarumal = datosSiembraYarumal[['Vereda','Arboles']]

print(datosYarumal)

crearTabla(datosYarumal,"tablaYarumal")




























#crearTabla(siembraTotal, "siembraTotal")

#graficarBarras(siembraTotal, 'Ciudad', 'Arboles', 'BarrasPruebaTotal')

## Esta no me funcionó
#graficarTorta(siembraTotal, [1, 5000, 10000, 15000, 20000, 30000], 'Ciudad', 'Arboles', 'TortaPruebaTotal')