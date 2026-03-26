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

    dadosSemOperador = dadosSemNulos[dadosSemNulos['Operador Empilhadeira'].isna()]
    placaOperador = dadosSemOperador['Placa'].tolist()
    printResultado("Sem Nome do Operador",placaOperador,dia,resultado)

    dadosSemHoraEntrada = dadosSemNulos[dadosSemNulos['Hora Entrada'].isna()]
    if len(dadosSemHoraEntrada) > 0:
        resultado += f"Sem Horário e Dia de Entrada - {dia}\n"
        for placa in dadosSemHoraEntrada['Placa'].tolist():
            resultado += f" - {placa}\n"
        resultado += "\n"

    dadosSemHoraEmissaoOC = dadosSemNulos[dadosSemNulos['Hora Emissão OC'].isna()]
    if len(dadosSemHoraEmissaoOC) > 0:
        resultado += f"Sem Horário e Dia da Emissão da OC - {dia}\n"
        for placa in dadosSemHoraEmissaoOC['Placa'].tolist():
            resultado += f" - {placa}\n"
        resultado += "\n"

    dadosSemHoraIniCarga = dadosSemNulos[dadosSemNulos['Hora Ini Carga'].isna()]
    if len(dadosSemHoraIniCarga) > 0:
        resultado += f"Sem Horário e Dia do Começo da Carga - {dia}\n"
        for placa in dadosSemHoraIniCarga['Placa'].tolist():
            resultado += f" - {placa}\n"
        resultado += "\n"

    dadosSemHoraFimCarga = dadosSemNulos[dadosSemNulos['Hora Fim Carga'].isna()]
    if len(dadosSemHoraFimCarga) > 0:
        resultado += f"Sem Horário e Dia do Fim da Carga - {dia}\n"
        for placa in dadosSemHoraFimCarga['Placa'].tolist():
            resultado += f" - {placa}\n"
        resultado += "\n"

    dadosSemHoraSaida = dadosSemNulos[dadosSemNulos['Hora Saída'].isna()]
    if len(dadosSemHoraSaida) > 0:
        resultado += f"Sem Horário e Dia de Saída - {dia}\n"
        for placa in dadosSemHoraSaida['Placa'].tolist():
            resultado += f" - {placa}\n"
        resultado += "\n"

    dadosSemNF = dadosSemNulos[dadosSemNulos['NF'].isna()]
    if len(dadosSemNF) > 0:
        resultado += f"Sem número NF - {dia}\n"
        for placa in dadosSemNF['Placa'].tolist():
            resultado += f" - {placa}\n"
        resultado += "\n"     

    return resultado

# Processamento
if arquivo and dia:
    try:
        dados = pd.read_excel(arquivo)
        resultado = analiseT2(dados, dia)

        # Exibir resultado em área de texto
        # st.text_area("Resultado da análise:", resultado, height=300)

        st.subheader("Resultado da análise:")
        # Botão que mostra o texto pronto para copiar
        # if st.button("📋 Mostrar texto para copiar"):
        st.code(resultado, language="text")


    except Exception as e:
        st.error(f"Erro ao processar o arquivo: {e}")

    return resultado

# Processamento
if arquivo and dia:
    try:
        dados = pd.read_excel(arquivo)
        resultado = analiseT2(dados, dia)

        # Exibir resultado em área de texto
        # st.text_area("Resultado da análise:", resultado, height=300)

        st.subheader("Resultado da análise:")
        # Botão que mostra o texto pronto para copiar
        # if st.button("📋 Mostrar texto para copiar"):
        st.code(resultado, language="text")


    except Exception as e:
        st.error(f"Erro ao processar o arquivo: {e}")

