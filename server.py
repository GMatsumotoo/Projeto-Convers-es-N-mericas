from flask import Flask, render_template, request

app = Flask(__name__)

def decimal_para_binario(decimal):
    try:
        return bin(decimal)
    except ValueError:
        return "Número inválido para conversão."

def decimal_para_hexadecimal(decimal):
    try:
        return hex(decimal)
    except ValueError:
        return "Número inválido para conversão."

def decimal_para_octal(decimal):
    try:
        return oct(decimal)
    except ValueError:
        return "Número inválido para conversão."

def binario_para_decimal(binario):
    try:
        return int(binario, 2)
    except ValueError:
        return "Número binário inválido para conversão."

def hexadecimal_para_decimal(hexadecimal):
    try:
        return int(hexadecimal, 16)
    except ValueError:
        return "Número hexadecimal inválido para conversão."

def octal_para_decimal(octal):
    try:
        return int(octal, 8)
    except ValueError:
        return "Número octal inválido para conversão."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/converter', methods=['POST'])
def converter():
    opcao = request.form['opcao']
    numero = request.form['numero']

    if opcao == "1":
        resultado = decimal_para_binario(int(numero))
    elif opcao == "2":
        resultado = decimal_para_hexadecimal(int(numero))
    elif opcao == "3":
        resultado = decimal_para_octal(int(numero))
    elif opcao == "4":
        resultado = binario_para_decimal(numero)
    elif opcao == "5":
        resultado = hexadecimal_para_decimal(numero)
    elif opcao == "6":
        resultado = octal_para_decimal(numero)
    else:
        resultado = "Opção inválida. Por favor, escolha uma opção válida."

    return render_template('resultado.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
