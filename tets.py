import streamlit as st
import subprocess

# Caminhos para os scripts de relatórios separados por banco
sicoob_caminho = "D:\\PYTHON\\AUTOCOMP\\SISTEMA\\RELATORIO\\PROCESSO\\RELATORIO_TRANSF_SICOOB.py"
santander_caminho = "D:\\PYTHON\\AUTOCOMP\\SISTEMA\\RELATORIO\\PROCESSO\\RELATORIO_TRANSF_SANTANDER.py"
itau_caminho = "D:\\PYTHON\\AUTOCOMP\\SISTEMA\\RELATORIO\\PROCESSO\\RELATORIO_TRANSF_ITAU.py"
bradesco_caminho = "D:\\PYTHON\\AUTOCOMP\\SISTEMA\\RELATORIO\\PROCESSO\\RELATORIO_TRANSF_BRADESCO.py"
banco_do_brasil_caminho = "D:\\PYTHON\\AUTOCOMP\\SISTEMA\\RELATORIO\\PROCESSO\\RELATORIO_TRANSF_BANCOBRASIL.py"

# Caminho para o script de cooperados
caminho_script_relatorio_cooperados = "D:\\PYTHON\\AUTOCOMP\\SISTEMA\\RELATORIO\\PROCESSO\\RELATORIO_COOPERADO.py"

# Caminho para o script de concatenação de comprovantes
caminho_script_concat_comprovantes = "D:\\PYTHON\\AUTOCOMP\\SISTEMA\\RELATORIO\\PROCESSO\\CONCAT_RELATORIO_COMP.py"

# Caminho para o script de relatório analítico
caminho_script_relatorio_analitico = "D:\\PYTHON\\AUTOCOMP\\SISTEMA\\RELATORIO\\PROCESSO\\RELATORIO_ANALISE.py"

# Caminho para o script de separação de comprovantes
caminho_script_separar_comprovantes = "D:\\PYTHON\\AUTOCOMP\\SISTEMA\\RELATORIO\\PROCESSO\\SPLIT TRANSF.py"

# Caminho para o script de processar comprovantes
caminho_script_processar_comprovantes = "D:\\PYTHON\\AUTOCOMP\\SISTEMA\\RELATORIO\\PROCESSO\\PROCESSAR_GERAL.py"

def executar_script(caminho_script):
    try:
        resultado = subprocess.run(['python', caminho_script], check=True, capture_output=True, text=True)
        st.success(f"Script {caminho_script} executado com sucesso!")
    except Exception as e:
        st.error(f"Erro ao executar o script {caminho_script}: {e}")

def main():
    st.title("Sistema de Relatórios de Transferências")

    st.sidebar.title("Opções")

    selecionado = st.sidebar.selectbox(
        "Escolha a ação",
        [
            "SEPARAR COMPROVANTES",
            "RELATÓRIO COOPERADOS",
            "RELATÓRIO COMPROVANTES",
            "CONCATENAR RELATÓRIOS(COMPROV.)",
            "RELATÓRIO ANALÍTICO",
            "PROCESSAR COMPROVANTES"
        ]
    )

    if selecionado == "SEPARAR COMPROVANTES":
        st.subheader("Separar Comprovantes")
        if st.button("Executar Separar Comprovantes"):
            executar_script(caminho_script_separar_comprovantes)

    elif selecionado == "RELATÓRIO COOPERADOS":
        st.subheader("Relatório de Cooperados")
        if st.button("Executar Relatório de Cooperados"):
            executar_script(caminho_script_relatorio_cooperados)

    elif selecionado == "RELATÓRIO COMPROVANTES":
        st.subheader("Relatório de Comprovantes")
        banco = st.selectbox(
            "Escolha o Banco",
            ["SICOOB", "SANTANDER", "ITAU", "BRADESCO", "BANCO DO BRASIL"]
        )
        if st.button("Gerar Relatório"):
            if banco == "SICOOB":
                executar_script(sicoob_caminho)
            elif banco == "SANTANDER":
                executar_script(santander_caminho)
            elif banco == "ITAU":
                executar_script(itau_caminho)
            elif banco == "BRADESCO":
                executar_script(bradesco_caminho)
            elif banco == "BANCO DO BRASIL":
                executar_script(banco_do_brasil_caminho)

    elif selecionado == "CONCATENAR RELATÓRIOS(COMPROV.)":
        st.subheader("Concatenar Relatórios de Comprovantes")
        if st.button("Executar Concatenar Relatórios"):
            executar_script(caminho_script_concat_comprovantes)

    elif selecionado == "RELATÓRIO ANALÍTICO":
        st.subheader("Relatório Analítico")
        if st.button("Executar Relatório Analítico"):
            executar_script(caminho_script_relatorio_analitico)

    elif selecionado == "PROCESSAR COMPROVANTES":
        st.subheader("Processar Comprovantes")
        if st.button("Executar Processar Comprovantes"):
            executar_script(caminho_script_processar_comprovantes)

if __name__ == "__main__":
    main()
