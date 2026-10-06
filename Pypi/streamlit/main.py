import streamlit as st
import pandas as pd

st.title("Painel Interativo de Exemplo")

# Entrada lateral (Sidebar)
st.sidebar.header("Configurações")
opcao = st.sidebar.selectbox("Escolha uma opção:", ["Visão Geral", "Dados"])

if opcao == "Visão Geral":
    st.subheader("Entrada de Dados")
    numero = st.slider("Selecione um valor:", min_value=1, max_value=100, value=50)
    st.write(f"O valor selecionado foi: **{numero}**")

elif opcao == "Dados":
    st.subheader("Tabela e Gráfico")
    
    # Criando dados fictícios
    dados = pd.DataFrame({
        'Vendas': [10, 20, 15, 30, 25],
        'Meses': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai']
    })
    
    # Exibindo a tabela e o gráfico de linhas
    st.dataframe(dados)
    st.line_chart(dados.set_index('Meses'))