from flask import Flask, render_template

app = Flask(__name__)

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console


@app.route("/jogos")
def jogos():
    jogo1 = Jogo("God of War", "Hack n Slash", "PS3")
    jogo2 = Jogo("Skyrim", "RPG", "PC")
    jogo3 = Jogo("Chrono Trigger", "RPG", "Nintendo DS")

    jogos = [jogo1, jogo2, jogo3]

    return render_template("jogos.html", titulo="Jogos", litaJogos=jogos)













app.run(debug = True)