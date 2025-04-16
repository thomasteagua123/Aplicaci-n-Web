from flask import Flask, url_for
import sqlite3

app = Flask(__name__)
db = None

def abrirConexiones():
    global db
    db = sqlite3.connect("instance/datos.sqlite")
    db.row_factory=sqlite3.Row
    return db

def cerrarConexiones():
    global db
    if db is not None:
        db.close()
        db=None

@app.route("/usuarios/")
def obtenerGente():
    global db
    conexion = abrirConexiones()
    cursor = conexion.cursor()
    cursor.execute=("SELECT * FROM usuarios")
    resultado= cursor.fetchall()
    cerrarConexiones()
    fila = [dict(row) for row in resultado]
    return str(fila)

# @app.route("/rutas")
# def rutas():
#     url_hola=
# @app.route("/")
# def principal():
#     return """ \
    
#     <a href='/chau'>chau</a>
#     <a href='/hola'>hola</a>

#     """

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

@app.route("/")
def main():
    url_hola = url_for("saludar")
    # url_dado = url_for("dado", cara=6)
    url_logo = url_for("static", filename="momo.jpeg" )
    
    return f"""
    <a href="{url_hola}">Hola</a>
    <br>
    <a href="{url_for("despedir")}">Chau</a>
    <br>
    <a href="{url_logo}" target="_blank">Logo</a>
    <br>
   

    """


