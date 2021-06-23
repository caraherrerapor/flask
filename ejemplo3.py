from flask import Flask,render_template,request


app = Flask(__name__)

@app.route("/")
def basico():
    return render_template('basico.html')

@app.route("/pagina1")
def pagina1():
    return render_template('pagina1.html')


@app.route("/pagina2")
def pagina2():
    return render_template('pagina2.html')


@app.route("/formulario")
def formulario():
    return render_template('formulario.html')

@app.route("/gracias")
def gracias():
    valor1 = request.args.get('nombre')
    valor2 = request.args.get('apellido')
    return render_template('gracias.html',nombre=valor1,apellido=valor2)

@app.errorhandler(404)
def not_found(e):
    return render_template('not_found.html'),404

@app.route("/formulario2")
def formulario2():
    return render_template('formulario2.html')

@app.route("/resultado")
def resultado():
    
    nombre = request.args.get('nombre')

    mayuscula = nombre[0].isupper() 
    minusculas = any(letra.islower() for letra in nombre)
    alfanum = any(letra.isdigit() for letra in nombre)
    todo = mayuscula and minusculas and alfanum
    
        
    return render_template('resultado.html',mayuscula=mayuscula,minusculas=minusculas,
                            alfanum=alfanum,todo=todo)    


if __name__ == '__main__':
    app.run(debug=True)