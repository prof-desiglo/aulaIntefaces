from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from hora import registrar_hora

app = Flask(__name__)
CORS(app)

@app.route('/valores', methods=['GET'])
def test():
    return jsonify([{"id": '01', "Nome_da_maquina":"localhost","ip": "127.0.0.1"},
                    {"id": '02', "Nome_da_maquina":"web","ip": "127.0.0.2"}])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/2')
def home2():
    return render_template('index2.html')

@app.route('/3')
def home3():
    return render_template('index3.html')

@app.route('/atualizaArquivo')
def executa():
    valor = registrar_hora("run.txt")
    resultado = {'resultado': valor}
    return jsonify(resultado)

