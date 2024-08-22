from flask import Flask, render_template, request, redirect

app = Flask(__name__)  # Cria uma instância da aplicação Flask

filmes = []

@app.route('/')  # Define uma rota padrão (página inicial) da aplicação
def index():
    return render_template('index
    filmes=filmes)



@app.route('/adicionar')  # Define uma rota padrão (página inicial) da aplicação
def adicionar():
    return render_template('adicionar.html', filmes=filmes)


@app.route('/adicionar_filme', methods=['GET', 'POST'])
def adicionar_filme():
    if request.method == 'POST':
        nome = request.form['nome']
        genero = request.form['genero']
        autor = request.form['autor']
        codigo = len(filmes)
        filmes.append([codigo, nome, genero, autor])
        return render_template('index.html', filmes=filmes)
    else:
        return redirect('/')  # Redireciona de volta para a página inicial

@app.route('/editar_filme/<int:codigo>', methods=['GET', 'POST'])
def editar_filme(codigo):
    if request.method == 'POST':
        nome = request.form['nome']
        genero = request.form['gênero']
        autor = request.form['autor']
        return redirect('/')  # Redireciona de volta para a página inicial
    else:
        filme = filmes[codigo]
        return render_template('editar.html', filme=filme)  # Renderiza o formulário de edição

@app.route('/apagar_filme/<int:codigo>')
def apagar_filme(codigo):
    del filmes[codigo]
    return redirect('/')


if __name__ == '__main__':  # Verifica se este arquivo está sendo executado diretamente
    app.run(debug=True)  # Inicia o servidor de desenvolvimento do Flask com modo de depuração ativado