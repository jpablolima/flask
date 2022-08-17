from flask import Flask, render_template

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console



app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/inicio')
def hello_world():
    jogo1 = Jogo('God of War','Hack n slash', 'PS5')
    jogo2 = Jogo('Skyrim','RPG', 'PC')
    jogo3 = Jogo('PES','Esporte', 'PS2')
    lista = [jogo1, jogo2, jogo3]
    return render_template('jogos.html', titulo='Jogos', jogos=lista)


app.run(debug=True)
