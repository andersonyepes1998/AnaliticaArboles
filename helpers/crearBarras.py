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
