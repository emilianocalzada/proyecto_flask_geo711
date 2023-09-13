from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    edad = 18
    return render_template('index.html', edad=edad, dato2=["1", "2", "3"])


@app.route('/contacto')
def contacto():
    return '<h1>Contacto</h2>'


@app.route('/proyectos/<nombre>/<int:edad>')
# @app.route('/proyectos/')
def proyectos(nombre, edad):
    return render_template('proyectos.html', nombre=nombre, edad=edad)


@app.route('/loops')
def loops():
    lista = ["Uno", "Dos", "Tres", "Cuatro"]
    return render_template('loops.html', lista=lista)


@app.route('/mapa/<float:lat>/<float(signed=True):long>/<cadena>')
def mapa(lat, long, cadena):
    long = float(long)
    return render_template('mapa.html', lat=lat, long=long, cadena=cadena)


if __name__ == '__main__':
    app.run()
