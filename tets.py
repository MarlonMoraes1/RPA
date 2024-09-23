import subprocess
import streamlit as st

# Funções para executar os scripts
def executar_script(caminho_script):
    try:
        # Executa o script e captura a saída
        resultado = subprocess.run(['python', caminho_script], check=True, capture_output=True, text=True)
        return resultado.stdout
    except subprocess.CalledProcessError as e:
        return f"Erro ao executar o script: {e.stderr}"

# Caminhos para os scripts
scripts = {
    "SEPARAR COMPROVANTES": "D:\\PYTHON\\AUTOCOMP\\SISTEMA\\RELATORIO\\PROCESSO\\SPLIT TRANSF.py",
    "RELATÓRIO COOPERADOS": "D:\\PYTHON\\AUTOCOMP\\SISTEMA\\RELATORIO\\PROCESSO\\RELATORIO_COOPERADO.py",
    "RELATÓRIO COMPROVANTES": "D:\\PYTHON\\AUTOCOMP\\SISTEMA\\RELATORIO\\PROCESSO\\RELATORIO_COMPROVANTES.py",
    "CONCATENAR RELATÓRIOS (COMPROV.)": "D:\\PYTHON\\AUTOCOMP\\SISTEMA\\RELATORIO\\PROCESSO\\CONCAT_RELATORIO_COMP.py",
    "RELATÓRIO ANALÍTICO": "D:\\PYTHON\\AUTOCOMP\\SISTEMA\\RELATORIO\\PROCESSO\\RELATORIO_ANALISE.py",
    "PROCESSAR COMPROVANTES": "D:\\PYTHON\\AUTOCOMP\\SISTEMA\\RELATORIO\\PROCESSO\\PROCESSAR_GERAL.py"
}

# Título da aplicação
st.title("Automação de Relatórios")

# Exibe um botão para cada função
for funcao, caminho in scripts.items():
    if st.button(funcao):
        resultado = executar_script(caminho)
        st.text_area(f"Resultado de {funcao}:", value=resultado, height=300)
