from flask import Flask


app = Flask("__name__")

#ruta
@app.route("/")

#lo que se va a mostrar
def principal():
    return "hola"


#nueva ruta
@app.route("/adios")
#fucion que va a dar servicio a esa ruta
def adios():
    return "adios"

#ruta dinamica
@app.route("/saludar/<nombre>")
def saludar(nombre):
    #return "hola {} buenos dias".format(nombre)
    return "la letra en la posicion 5 es {}".format(nombre[5])

#ruta dinamica2
@app.route("/longitud/<palabra>")
def longitud(palabra):
    valor =len(palabra)
    return "la longitud de {} es {}".format(palabra,valor)

#ruta dinamica3
@app.route("/edad/<nombre>/<anos>")
def dobleDato(nombre,anos):
    return "{} tiene {} anos".format(nombre,anos)

#ruta dinamica4
@app.route("/sumar/<num1>/<num2>")
def suma(num1,num2):
    n1 = int(num1)
    n2 = int(num2)
    t = n1+n2
    return "la suma de {} y {} es {}".format(n1,n2,str(t))





if __name__ == '__main__':
    app.run(debug=True)
