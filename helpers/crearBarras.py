import matplotlib.pyplot as plt

def graficarBarras(dataFrame, campoX, campoY, nombreGrafica):
    colores = ['teal', 'purple', 'darkblue', 'green', 'orange']
    siembraArboles = dataFrame.groupby(campoX)[campoY].mean()

    # Generar grafica
    plt.bar(siembraArboles.index, siembraArboles, color=colores)

    plt.title("Siembra Total")
    plt.xlabel("Municipio")
    plt.ylabel("Arboles")

    plt.savefig(f'./graficas/barras/{nombreGrafica}.png')


def graficasBarrasSantaFe(dataFrame, campoX, campoY, nombreGraficaSantaFe):
    colores = ['teal', 'purple', 'darkblue', 'green', 'orange']
    siembraArbolesSantafe = dataFrame.groupby(campoX)[campoY].mean()

    # Generar grafica
    plt.bar(siembraArbolesSantafe.index, siembraArbolesSantafe, color=colores)

    plt.title("tabla")
    plt.xlabel("Municipio")
    plt.ylabel("Arboles")

    plt.savefig(f'./graficas/barras/{nombreGraficaSantaFe}.png')