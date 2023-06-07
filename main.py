import pandas as pd
from helpers.crearTablas import crearTabla
from helpers.crearBarras import graficarBarras
from helpers.crearTorta import graficarTorta

tablaSiembra = pd.read_csv("./data/Siembras.csv")

siembraTotal = tablaSiembra.query("Arboles > 0")

siembraMedellin = tablaSiembra.query("Ciudad == 'Medellín'")

#crearTabla(siembraTotal, "siembraTotal")

#graficarBarras(siembraTotal, 'Ciudad', 'Arboles', 'BarrasPruebaTotal')

## Esta no me funcionó
#graficarTorta(siembraTotal, [1, 5000, 10000, 15000, 20000, 30000], 'Ciudad', 'Arboles', 'TortaPruebaTotal')