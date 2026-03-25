from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

def analiseT2(dados, dia):
    baixoT2 = 10
    altoT2 = 60

    dadosSemNulos = dados[dados["Senha Válida?"] != "Em Aberto"]
    filtroT2 = (dadosSemNulos["T2 - Carregamento"] > altoT2) | (dadosSemNulos["T2 - Carregamento"] < baixoT2)
    dadosFiltrados = dadosSemNulos[filtroT2]

    placas = dadosFiltrados["Placa"].tolist()
    tempo = dadosFiltrados["T2 - Carregamento"].tolist()

    resultado = ""
    if len(placas) > 0:
        resultado += f"Inconsistências T2 - {dia}\n"
        for i in range(len(placas)):
            resultado += f"{placas[i]} - T2 em {tempo[i]} min\n"
        resultado += "\n"

    return resultado

@app.route("/", methods=["GET", "POST"])
def upload_file():
    resultado = ""
    if request.method == "POST":
        arquivo = request.files["file"]
        dia = request.form.get("dia")

        try:
            dados = pd.read_excel(arquivo)
            resultado = analiseT2(dados, dia)
        except Exception as e:
            resultado = f"Erro ao processar o arquivo: {e}"

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
