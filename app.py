from flask import Flask, url_for

app = Flask(__name__)

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
    url_logo = url_for("static", filename="momo.jpeg")
    
    return f"""
    <a href="{url_hola}">Hola</a>
    <br>
    <a href="{url_for("despedir")}">Chau</a>
    <br>
    <a href="{url_logo}">Logo</a>
    <br>
   

    """


