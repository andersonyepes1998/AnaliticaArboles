import pandas as pd
import matplotlib.pyplot as plt


def graficarTorta(dataFrame, rangos, columnaInteres, columnaPromediar, nombreGrafica):
    plt.figure()

    dataFrame['rangosSiembra'] = pd.cut(dataFrame[columnaInteres],  bins=rangos)

    siembraPorRango = dataFrame.groupby('rangosSiembra')[columnaPromediar].sum()

    # Definimos los datos a graficar
    siembra = siembraPorRango.values
    rangosSiembra = siembraPorRango.index

    plt.pie(siembra, labels=rangosSiembra, autopct='%1.1f%%')
    plt.title("Siembra por rango de cantidad")
    plt.savefig(f'./graficas/tortas/{nombreGrafica}.png')
