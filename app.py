from flask import Flask, render_template, g
import sqlite3
gi
app = Flask("Olá Mundo")

DATABASE = "banco.bd"
SECRET_KEY = "1234"

app = Flask("Olá Mundo")

app.config.from_object(__name__)

def conectar():
    return sqlite3.connect(DATABASE)

@app.before_request
def before_request():
    g.bd = conectar()

@app.teardown_request
def teardown_request(f):
    g.bd.close()

@app.route("/")
def exibir_posts():
    sql = "SELECT titulo, texto, data_criacao FROM posts ORDER BY id DESC"
    resultado = g.bd.execute(sql)

    post = {"titulo":"Meu Título", "texto":"Primeiro texto","data_criacao":"23/11/2022"}
    return render_template("hello.html", post = posts)

