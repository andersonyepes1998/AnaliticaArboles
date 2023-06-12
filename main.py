import pandas as pd
import matplotlib as plt
from helpers.crearBarras import graficasYarumal
from helpers.crearBarras import graficasBarrasSantaFe
from helpers.crearBarras import graficasBelmira
from helpers.crearBarras import graficasBelmiraLaSalazar
from helpers.crearBarras import graficasCaramanta
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

datos = datosSiembra[['Vereda','Arboles']]
print(datos)

#Aqui pintamos la tabala
#crearTablaSantaFe(datos,"tabla")

#Aqui pintamos la grafica

#graficasBarrasSantaFe(datos,'Vereda','Arboles','tabla Siembra Santa fe Antioquia')



##FILTRO TRES BELMIRA###

tablaSiembraBelmira = pd.read_csv("./data/Siembras.csv")

# print(tablaSiembraSantafe)
datosSiembraBe = tablaSiembraBelmira.query('Vereda == "Rio Arriba" and Arboles>0')
datosSiembraBe2 = tablaSiembraBelmira.query('Vereda == "La Salazar" and Arboles>0')

datosBelmira = datosSiembraBe[['Vereda','Hectareas']]
datosBelmira2 = datosSiembraBe2[['Vereda','Hectareas']]
print(datosBelmira)
print('\n')
print(datosBelmira2)
print('\n')

# crearTabla(datosBelmira,"tablaBelmira1")
# crearTabla(datosBelmira2,"tablaBelmira2")

#Aqui la creacion de la grafica
# graficasBelmira(datosBelmira,'Vereda', 'Hectareas', 'Tabla Siembra de Belmira')
# graficasBelmiraLaSalazar(datosBelmira2, 'Vereda', 'Hectareas', 'Tabla Siembra de Belmira la Salazar')




##FILTRO CINCO CARAMANTA###

tablaSiembraCaramanta = pd.read_csv("./data/Siembras.csv")

datosSiembraCaramanta = tablaSiembraCaramanta.query('Arboles>100')

datosCara = datosSiembraCaramanta[['Vereda','Arboles']]

print(datosCara)
print('\n')

# crearTabla(datosCara,"tablaCaramanta")

#Aqui esta la graficas

#graficasCaramanta(datosCara,'Vereda','Arboles','Tabla Siembra de Caramanta')





##FILTRO SEIX YARUMAL###

tablaSiembraYarumal = pd.read_csv("./data/Siembras.csv")

datosSiembraYarumal = tablaSiembraYarumal.query('Vereda == "Mallarino" and Arboles>0')

datosYarumal = datosSiembraYarumal[['Arboles','Hectareas']]

print(datosYarumal)

# crearTabla(datosYarumal,"tablaYarumal")

#Aqui esta la graficas

graficasYarumal(datosYarumal,'Arboles','Hectareas','Tabla Siembra de Yarumal')































#crearTabla(siembraTotal, "siembraTotal")

#graficarBarras(siembraTotal, 'Ciudad', 'Arboles', 'BarrasPruebaTotal')

## Esta no me funcionó
#graficarTorta(siembraTotal, [1, 5000, 10000, 15000, 20000, 30000], 'Ciudad', 'Arboles', 'TortaPruebaTotal')