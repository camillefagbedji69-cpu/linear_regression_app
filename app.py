import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

st.title("🌱 Analyse écologique interactive")

# Upload de fichier
uploaded_file = st.file_uploader("📂 Chargez un fichier CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file, sep = ";")
    st.write("Aperçu des données :", df.head())

    # Sélection des colonnes
    colonnes = df.columns.tolist()
    x_col = st.selectbox("Variable explicative (X)", colonnes)
    y_col = st.selectbox("Variable à expliquer (Y)", colonnes)

    # Graphique
    fig, ax = plt.subplots()
    sns.scatterplot(x=df[x_col], y=df[y_col], ax=ax)
    st.pyplot(fig)

    # Régression
    X = sm.add_constant(df[x_col])  # constante
    model = sm.OLS(df[y_col], X).fit()
    st.write("📊 Résultats de la régression :")
    st.write(model.summary())



