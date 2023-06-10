import pandas as pd

tablaSiembraBelmira = pd.read_csv("./data/Siembras.csv")

# print(tablaSiembraSantafe)
datosSiembraBe = tablaSiembraBelmira.query('Vereda == "Rio Arriba" and Vereda=="La Salazar"')

datosBelmira = datosSiembraBe[['Vereda']]
print(datosBelmira)
