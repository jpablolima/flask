from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/inicio')
def hello_world():
    return render_template('jogos.html', titulo='Jogos')


app.run(debug=True)
