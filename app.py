from flask import Flask, render_template,redirect, request, session
from bd import BD

app = Flask(__name__)
bd = BD()

app.secret_key = '123'
user = {}

@app.route('/')
def index():
    contatos = bd.buscaContatos()
    return render_template('index.html', contatos=contatos)



@app.roude("/deletar/str:<telefoneContato>")
def deletar (telefoneContato):
    bd.deletarcontato()
    
@app.roude("/novocontato", methods=["POST"])
def novocontat():
    nome = request.form["nome"]
    telefone = request.form["telefone"]
    cidade= request.form["cidade"]    
    
     
@app.route('/lista')
def logar():
    session['origem'] = 'lista'
    return render_template('lista.html')
    

if __name__ == '__main__':
    app.run(debug=True)
