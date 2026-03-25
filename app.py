import pandas as pd
import streamlit as st

# Configuração da página
st.set_page_config(page_title="Analisador de Arquivos Excel", layout="wide")

# Título
st.title("📊 Analisador de Arquivos Excel")

# Entrada do dia
dia = st.text_input("Digite o dia da consulta:")

# Upload do arquivo Excel
arquivo = st.file_uploader("Selecione o arquivo Excel", type=["xlsx", "xls"])

# Função de análise
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

# Processamento
if arquivo and dia:
    try:
        dados = pd.read_excel(arquivo)
        resultado = analiseT2(dados, dia)

        # Exibir resultado
        st.text_area("Resultado da análise:", resultado, height=300, key="resultado_area")

        # Botão de copiar usando JavaScript
        copy_code = f"""
        <button onclick="navigator.clipboard.writeText(`{resultado}`)">📋 Copiar Resultado</button>
        """
        st.markdown(copy_code, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Erro ao processar o arquivo: {e}")

