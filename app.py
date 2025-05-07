from flask import Flask, url_for, render_template
import sqlite3

app = Flask(__name__)
db = None


def dict_factory(cursor, row):
  """Arma un diccionario con los valores de la fila."""
  fields = [column[0] for column in cursor.description]
  return {key: value for key, value in zip(fields, row)}


def abrirConexion():
   global db
   db = sqlite3.connect("instance/datos.sqlite")
   db.row_factory = dict_factory
   return db

def cerrarConexion():
   global db
   if db is not None:
    db.close()
    db = None

@app.route("/sqlite/test-db")
def testDB():
   abrirConexion()
   cursor = db.cursor()
   cursor.execute("SELECT COUNT(*) AS cant FROM usuarios; ")
   res = cursor.fetchone() #Proximo registro y el fetchall devuelve todos los registros que quedan en una lista
   registros = res["cant"]
   cerrarConexion()
   return f"Hay {registros} registros en la tabla usuarios"

@app.route("/crear-usuario")
def testCrear():
    nombre = "Paco"
    email = "pacotero@gmail.com"
    abrirConexion()
    cursor = db.cursor()
    consulta = "INSERT INTO usuario(usuario)"


@app.route("/")
def main():
    url_hola = url_for("hello")
    url_dado = url_for("dado", caras=6)
    url_logo = url_for("static", filename="img/logo.png")
    url_sumar = url_for("suma", n1 = 1, n2 =9)
    url_palidromo = url_for("es_palidromo", palabra = str(""))

    return f"""
    <a href="{url_hola}">Hola</a>
    <br>
    <a href="{url_for("bye")}">Chau</a>
    <br>
    <a href="{url_logo}">Logo</a>
    <br>
    <a href="{url_dado}">Tirar_dados</>
    <br>
    <a href="{url_sumar}">Sumar dos numeros</>
    <br>
    <a href="{url_palidromo}">Saber si una palabra es palidromo o no</>
    """

@app.route("/saludar/hola")
def hello():
    return """
    <p>Hola</p>
    <br>
    <a href="saludar/chau">Chau</a>
    <br>
    <a href="chau">Chau 2</a>
    """

@app.route("/saludar/chau")
def bye():
    return "<p>Chau</p>"

@app.route("/saludar/por-nombre/<string:nombre>")
def sxn(nombre):
    return "<p>Chau</p>"

@app.route("/hello world")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hola mundo")
def hola_mundo():
    return "<p>hola mundo</p>"

@app.route("/tirar-dado/<int:caras>")
def dado(caras):
    from random import randint
    n = randint(1,caras)
    return f"<p>Tire un dado de {caras} caras, salio {n}<p>"

@app.route("/sumar/<int:n1>/<int:n2>")
def suma(n1,n2):
    suma = n1 + n2
    return f"<h2>{n1}+{n2}={suma}"

@app.route("/palidromo/<string:palabra>")
def es_palidromo(palabra):
    palabra_limpia = palabra.lower().replace(" ", " ")
    es_pal = palabra_limpia == palabra_limpia[::-1]
    resultado = "es "if es_pal else "no es"
    return f"<h2> La Palabra '{palabra}' {resultado} un palidromo. <h2/>"

@app.route("/usuarios/")
def obtenerGente():
    global db
    conexion = abrirConexion()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM usuarios')
    resultado = cursor.fetchall()
    cerrarConexion()
    fila = [dict(row) for row in resultado]
    return str(fila)

@app.route("/sqlite/delete/<int:id>")
def testDelete(id):
    abrirConexion()
    db.cursor()
    db.execute("DELETE FROM usuarios WHERE id= ?", (id,))
    db.commit()
    cerrarConexion()
    return f"Se borro el id {id} en la tabla de usuarios."


@app.route("/sqlite/agregar/<string:usuario>/<string:email>")
def testAgregar(usuario, email):
    abrirConexion()
    db.cursor()
    db.execute("INSERT INTO usuarios(usuario, email) VALUES (?, ?)", (usuario, email))
    db.commit()
    cerrarConexion()
    return f"Se agragó el usuario {usuario} en la tabla de usuarios"

@app.route("/sqlite/detalle/<int:id>")
def testDetalle(id):
    conexion = abrirConexion()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM usuarios')
    resultado = cursor.fetchone()
    cerrarConexion()
    fila = dict(resultado)
    return str(fila)

@app.route("/sqlite/cambiar-email/<string:usuario>/<string:email>")
def testUpdate(usuario, email):
    abrirConexion()
    db.cursor()
    db.execute("UPDATE usuarios set email=? WHERE usuario = ?;", (email,usuario))
    db.commit()
    cerrarConexion()
    return f"Se cambio el email {email} de {usuario}"
    

@app.route("/mostrar-datos-plantilla/<int:id>")
def datos_plantilla(id):
    abrirConexion()
    cursor = db.cursor()
    cursor.execute("SELECT id, usuario, email FROM usuarios WHERE id = ?; ", (id,))
    res = cursor.fetchone()
    cerrarConexion()
    usuario = None
    email = None
    if res != None:
        usuario=res['usuario']
        email=res['email']
    return render_template("datos.html", id=id, usuario=usuario, email=email)
