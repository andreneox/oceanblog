from flask import Flask, render_template
from datetime import datetime

app = Flask ("hello")

posts = [
        {
            "title" : "Meu primeiro post",
            "body" : "Aqui e o texto do post",
            "author" : "Andre",
            "created" : datetime(2022, 7, 25)
        },
         {
            "title" : "Meu segundo post",
            "body" : "Aqui e o texto do post",
            "author" : "Jojo",
            "created" : datetime(2022, 7, 26)
        },
]

@app.route ("/")
def index(): 
    return render_template ("index.html", posts=posts)

@app.route ("/login")
def login(): 
    return render_template ("login.html", posts=posts)
