import pandas as pd

import streamlit as st



st.image("/home/dscoliveira/Projects/NHL/images/NHL_LOGO.png", width=300)
st.title("Analise Exploratoria de Dados - NHL")
st.image("/home/dscoliveira/Projects/NHL/images/web_hockey_basen_art.jpg", width=450)



# importando os dados
nhl_eda = pd.read_csv("/home/dscoliveira/Projects/NHL/datasets/nhl_eda_cleaned.csv")


# Numero de linha
st.markdown("**Dimensao do conjunto de dados:**")
st.write("Numero de observacoes:", nhl_eda.shape[0])
st.write("Numero de linhas", nhl_eda.shape[1])
st.markdown('**Visualizando o dataframe**')
number = st.slider('Escolha o numero de colunas que deseja ver', min_value=1, max_value=20)
st.dataframe(nhl_eda.head(number))
st.markdown("**Resumo estatistico**")
st.write(nhl_eda[["goals_for","shots","hits"]].describe())
