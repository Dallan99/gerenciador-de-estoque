from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista para armazenar as motos cadastradas (temporário)
motos = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adicionar_moto', methods=['GET', 'POST'])
def adicionar_moto():
    if request.method == 'POST':
        modelo = request.form['modelo']
        ano = request.form['ano']
        cor = request.form['cor']
        marca = request.form['marca']
        placa = request.form['placa']
        valor_compra = request.form['valor_compra']
        valor_venda = request.form['valor_venda']

        # Adicionando moto na lista
        motos.append({
            'modelo': modelo,
            'ano': ano,
            'cor': cor,
            'marca': marca,
            'placa': placa,
            'valor_compra': valor_compra,
            'valor_venda': valor_venda
        })

        return redirect('/estoque')

    return render_template('adicionar_moto.html')

@app.route('/estoque')
def estoque():
    return render_template('estoque.html', motos=motos)

if __name__ == '__main__':
    app.run(debug=True)
