from crypt import methods
from curses import flash
from flask import Flask, render_template, request, redirect, session, flash

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console

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
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/jogos')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if 'bazinga' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + 'com sucesso!')
        return redirect('/jogos')
    else:
        flash('Erro no login, verifique usuário e senha !')
        return redirect('/login')

app.run(debug=True)
