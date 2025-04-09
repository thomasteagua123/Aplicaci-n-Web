from flask import Flask

app = Flask(__name__)

@app.route("/")
def principal():
    return """ \
    
    <a href='/chau'>chau</a>
    <a href='/hola'>hola</a>

    """

@app.route("/hola")
def saludar():
    return '<h2>hola</h2>'

@app.route("/chau")
def despedir():
    return '<h2>chau</h2>'

@app.route("/hola/<string:nombre>")
def saludar_con_nombre(nombre):
    return f"<h2>hola {nombre}, como estás?</h2>"

@app.route("/chau/<string:pepe>")
def despedir_con_nombre(pepe):
    return f"<h2>chau {pepe}, nos vemos.</h2>"
