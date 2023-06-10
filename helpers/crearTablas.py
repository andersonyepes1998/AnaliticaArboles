def crearTabla(dataFrame, nombreTabla):
    archivoHtml = dataFrame.to_html()  # Aqui tengo el DF version html
    # Tengo un archivo html vacio
    archivo = open(f"./tablas/{nombreTabla}.html", "w")
    archivo.write(''' 
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>Tablas</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
        </head>
        <body>           
    ''')
    archivo.write(archivoHtml)
    archivo.write(''' 
        </body>
        </html>
    ''')
    archivo.close()


def crearTablaSantaFe(dataFrame, nombreTablaSanta):
    archivoHtml = dataFrame.to_html()  # Aqui tengo el DF version html
    # Tengo un archivo html vacio
    archivo = open(f"./tablas/{nombreTablaSanta}.html", "w")
    archivo.write(''' 
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>Tablas</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
        </head>
        <body>           
    ''')
    archivo.write(archivoHtml)
    archivo.write(''' 
        </body>
        </html>
    ''')
    archivo.close()
