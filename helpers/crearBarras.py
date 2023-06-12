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

    plt.title("tabla Siembra Santa fe Antioquia")
    plt.xlabel("Vereda")
    plt.ylabel("Arboles")

    plt.savefig(f'./graficas/barras/{nombreGraficaSantaFe}.png')



def graficasBelmira(dataFrame, campoX, campoY, nombreGraficaBelmira):
    colores = ['teal', 'purple', 'darkblue', 'green', 'orange']
    siembraArbolesBelmira = dataFrame.groupby(campoX)[campoY].mean()

    # Generar grafica
    plt.bar(siembraArbolesBelmira.index, siembraArbolesBelmira, color=colores)

    plt.title("Tabla Siembra de Belmira Rio Arriba")
    plt.xlabel("Vereda")
    plt.ylabel("Hectareas")

    plt.savefig(f'./graficas/barras/{nombreGraficaBelmira}.png')



def graficasBelmiraLaSalazar(dataFrame, campoX, campoY, nombreGraficaBelmiraLaSalazar):
    colores = ['teal', 'purple', 'darkblue']
    siembraArbolesBelmiraLaSalazar = dataFrame.groupby(campoX)[campoY].mean()

    # Generar grafica
    plt.bar(siembraArbolesBelmiraLaSalazar.index, siembraArbolesBelmiraLaSalazar, color=colores)

    plt.title("Tabla Siembra de Belmira la Salazar")
    plt.xlabel("Vereda")
    plt.ylabel("Hectareas")

    plt.savefig(f'./graficas/barras/{nombreGraficaBelmiraLaSalazar}.png')


def graficasCaramanta(dataFrame, campoX, campoY, nombreGraficaCaramanta):
    colores = ['teal', 'purple', 'darkblue']
    siembraArbolesCaramanta = dataFrame.groupby(campoX)[campoY].mean()

    # Generar grafica
    plt.bar(siembraArbolesCaramanta.index, siembraArbolesCaramanta, color=colores)

    plt.title("Tabla Siembra de Caramanta")
    plt.xlabel("Vereda")
    plt.ylabel("Arboles")

    plt.savefig(f'./graficas/barras/{nombreGraficaCaramanta}.png')



def graficasYarumal(dataFrame, campoX, campoY, nombreGraficaYarumal):
    colores = ['teal', 'purple', 'darkblue','green', 'orange']
    siembraArbolesYarumal = dataFrame.groupby(campoX)[campoY].mean()

    # Generar grafica
    plt.bar(siembraArbolesYarumal.index, siembraArbolesYarumal, color=colores)

    plt.title("Tabla Siembra de Yarumal")
    plt.xlabel("Arboles")
    plt.ylabel("Hectareas")

    plt.savefig(f'./graficas/barras/{nombreGraficaYarumal}.png')