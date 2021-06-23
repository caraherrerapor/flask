from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def portada():
    return render_template("index.html")

@app.route("/hola")
def hola():
    
    diccionario = {'nombre':'carlos','edad':'34','color':'azul'}
    return render_template("hola.html",datos = diccionario)

@app.route("/colores")
def colores():
    lista_colores = ['azul','rojo','verde','amarillo']
    
    return render_template("colores.html",colores =lista_colores )

@app.route("/frases/<texto>")
def frases(texto):
    return render_template("frases.html",tipo=texto)




if __name__ == '__main__':
    app.run(debug = True)
    
