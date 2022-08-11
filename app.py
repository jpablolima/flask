from crypt import methods
from curses import flash
import re
from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'gandalf'


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo("God of War", "Hack n Slash", "PS3")
jogo2 = Jogo("Skyrim", "RPG", "PC")
jogo3 = Jogo("Chrono Trigger", "RPG", "Nintendo DS")
lista = [jogo1, jogo2, jogo3]


@app.route('/home')
def home():
    return render_template("index.html", titulo="Games")


@app.route("/jogos")
def jogos():
    return render_template("jogos.html", titulo="Jogos", listaJogos=lista)


@app.route("/novojogo")
def novojogo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=novo')
    return render_template('novojogo.html', titulo="Novo Jogo")


@app.route("/criarjogo", methods=['POST'])
def criarjogo():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)

    return redirect("/jogos")


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST'])
def autenticar():
    if 'bazinga' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + ' logado com sucesso!')
        proxima_pagina = request.form['proxima']
        return redirect('/jogos{}'.format(proxima_pagina))
        # return redirect('/jogos')
    else:
        flash('Erro no login!')
        return redirect('/login')
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect('/home')


app.run(debug=True)
