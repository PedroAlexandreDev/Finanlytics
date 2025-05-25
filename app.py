import streamlit as st
import os
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Finanlytics", layout="wide")

st.title("💼 Finanlytics — Controle Financeiro Interativo")

if not os.path.exists("dates"):
    os.makedirs("dates")

upload = st.file_uploader("📤 Faça o upload dos seus dados (CSV ou Excel):", type=["csv", "xlsx"])

if upload:
    file_name = upload.name
    save_path = os.path.join("dates", file_name)
    with open(save_path, "wb") as f:
        f.write(upload.getbuffer())
    st.success("✅ Arquivo salvo com sucesso!")

dataFrames = []
files = os.listdir("dates")

for file in files:
    path = os.path.join("dates", file)
    if file.endswith(".csv"):
        data = pd.read_csv(path)
    elif file.endswith(".xlsx"):
        data = pd.read_excel(path)
    else:
        st.warning(f"⚠️ Arquivo ignorado: {file}")
        continue
    dataFrames.append(data)

df_final = pd.concat(dataFrames, ignore_index=True)

# Processamento de colunas
df_final["Data"] = pd.to_datetime(df_final["Data"], errors="coerce")
df_final = df_final.dropna(subset=["Data", "Valor", "Categoria"])

df_final["Ano"] = df_final["Data"].dt.year
df_final["Mês"] = df_final["Data"].dt.to_period("M").astype(str)
df_final["Dia"] = df_final["Data"].dt.day

st.sidebar.subheader("📅 Filtro de Data")
data_inicial = df_final["Data"].min()
data_final = df_final["Data"].max()

inicio, fim = st.sidebar.date_input(
    "Selecione o intervalo:",
    value=(data_inicial, data_final),
    min_value=data_inicial,
    max_value=data_final
)

df_filtrado = df_final[(df_final["Data"] >= pd.to_datetime(inicio)) & (df_final["Data"] <= pd.to_datetime(fim))]

st.subheader("📋 Dados filtrados")
st.dataframe(df_filtrado, use_container_width=True)

total_valor = df_filtrado["Valor"].sum()
total_despesas = df_filtrado[df_filtrado["Valor"] < 0]["Valor"].sum()
total_receitas = df_filtrado[df_filtrado["Valor"] > 0]["Valor"].sum()

col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Geral", f"R$ {total_valor:,.2f}")
col2.metric("⬇️ Total de Despesas", f"R$ {total_despesas:,.2f}")
col3.metric("⬆️ Total de Receitas", f"R$ {total_receitas:,.2f}")

df_despesas = df_filtrado[df_filtrado["Valor"] < 0]
df_despesas_agg = df_despesas.groupby("Categoria")["Valor"].sum().abs().reset_index()

if not df_despesas_agg.empty:
    fig1 = px.pie(df_despesas_agg, names="Categoria", values="Valor", title="💸 Distribuição de Despesas por Categoria", hole=0.4)
    st.plotly_chart(fig1, use_container_width=True)

df_mensal = df_filtrado.groupby("Mês")["Valor"].sum().reset_index()
fig2 = px.bar(df_mensal, x="Mês", y="Valor", title="📊 Saldo por Mês", text_auto=".2s")
st.plotly_chart(fig2, use_container_width=True)

df_diario = df_filtrado.groupby("Data")["Valor"].sum().reset_index()
fig3 = px.line(df_diario, x="Data", y="Valor", title="📈 Evolução Diária do Saldo", markers=True)
st.plotly_chart(fig3, use_container_width=True)

df_tipo = df_filtrado.copy()
df_tipo["Tipo"] = df_tipo["Valor"].apply(lambda x: "Receita" if x > 0 else "Despesa")
df_group = df_tipo.groupby(["Mês", "Tipo"])["Valor"].sum().reset_index()
fig4 = px.bar(df_group, x="Mês", y="Valor", color="Tipo", barmode="relative", title="📊 Receitas e Despesas por Mês")
st.plotly_chart(fig4, use_container_width=True)


st.download_button("⬇️ Exportar Dados Filtrados", df_filtrado.to_csv(index=False), "dados_filtrados.csv", "text/csv")