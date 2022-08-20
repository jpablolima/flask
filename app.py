from crypt import methods
from curses import flash
from flask import Flask, render_template, request, redirect, session, flash, url_for

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console

class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha

usuario1 = Usuario('João Pablo', 'jpablo','bazinga')
usuario2 = Usuario('Goku','goku', 'goku')
usuario3 = Usuario('Batman', 'batman', 'batman')
usuario4 = Usuario('Vegeta','vageta','vageta')
        
usuarios = { usuario1.nickname : usuario1, 
             usuario2.nickname : usuario2, 
             usuario3.nickname : usuario3,
             usuario4.nickname : usuario4
            }


jogo1 = Jogo('God of War','Hack n slash', 'PS5')
jogo2 = Jogo('Skyrim','RPG', 'PC')
jogo3 = Jogo('PES','Esporte', 'PS2')
lista = [jogo1, jogo2, jogo3]


app = Flask(__name__)
app.secret_key = 'games'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/jogos')
def lista_jogos():
    
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('lista_jogos'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)

    else:
        flash('Erro no login, verifique usuário e senha !')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('lista_jogos'))

app.run(debug=True)
