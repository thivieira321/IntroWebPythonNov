from flask import Flask, render_template

app = Flask("Olá")

@app.route("/")
def hello():
    return "Olá Mundo!"

@app.route("/alunos")
def alunos():
    return render_template("hello.html")

