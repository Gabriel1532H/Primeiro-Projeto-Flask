from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form.get('nome')
        idade = request.form.get('idade')

        return render_template("resultado.html", nome=nome, idade=idade)

    return render_template("index.html")

@app.route('/sobre')
def sobre():
    return "<h2>Este é um mini prjeto Flask com rotas, formulário e template.</h2>"
if __name__ == '__main__':
    app.run(debug=True)