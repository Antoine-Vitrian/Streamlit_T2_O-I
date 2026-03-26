import pandas as pd
import streamlit as st

# Configuração da página
st.set_page_config(page_title="Analisador de Arquivos Excel", layout="wide")

# Título
st.title("📊 Analisador de Arquivos Excel T2")

# Entrada do dia
dia = st.text_input("Digite o dia da consulta:")

# Upload do arquivo Excel
arquivo = st.file_uploader("Selecione o arquivo Excel", type=["xlsx", "xls"])

def printResultado(titulo, placas, dia, resultado):
    if placas:  # checa se não está vazia
        resultado += f"{titulo} - {dia}\n"
        for placa in placas:
            resultado += f" - {placa}\n"
        resultado += "\n"
    return resultado

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

    # Checando campos faltantes
    dadosSemOperador = dadosSemNulos[dadosSemNulos['Operador Empilhadeira'].isna()]
    resultado = printResultado("Sem Nome do Operador", dadosSemOperador['Placa'].tolist(), dia, resultado)

    dadosSemHoraEntrada = dadosSemNulos[dadosSemNulos['Hora Entrada'].isna()]
    resultado = printResultado("Sem Horário e Dia de Entrada", dadosSemHoraEntrada['Placa'].tolist(), dia, resultado)

    dadosSemHoraEmissaoOC = dadosSemNulos[dadosSemNulos['Hora Emissão OC'].isna()]
    resultado = printResultado("Sem Horário e Dia da Emissão da OC", dadosSemHoraEmissaoOC['Placa'].tolist(), dia, resultado)

    dadosSemHoraIniCarga = dadosSemNulos[dadosSemNulos['Hora Ini Carga'].isna()]
    resultado = printResultado("Sem Horário e Dia do Começo da Carga", dadosSemHoraIniCarga['Placa'].tolist(), dia, resultado)

    dadosSemHoraFimCarga = dadosSemNulos[dadosSemNulos['Hora Fim Carga'].isna()]
    resultado = printResultado("Sem Horário e Dia do Fim da Carga", dadosSemHoraFimCarga['Placa'].tolist(), dia, resultado)

    dadosSemHoraSaida = dadosSemNulos[dadosSemNulos['Hora Saída'].isna()]
    resultado = printResultado("Sem Horário e Dia de Saída", dadosSemHoraSaida['Placa'].tolist(), dia, resultado)

    dadosSemNF = dadosSemNulos[dadosSemNulos['NF'].isna()]
    resultado = printResultado("Sem número NF", dadosSemNF['Placa'].tolist(), dia, resultado)

    return resultado

# Processamento
if arquivo and dia:
    try:
        dados = pd.read_excel(arquivo)
        resultado = analiseT2(dados, dia)

        st.subheader("Resultado da análise:")
        st.code(resultado, language="text")

    except Exception as e:
        st.error(f"Erro ao processar o arquivo: {e}")
