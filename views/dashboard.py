import streamlit as st
from src.services.data_loader import carregar_dados
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

base = carregar_dados()


base["Data Chegada"] = pd.to_datetime(
    base["Data Chegada"], dayfirst=True, errors="coerce"
)

coluna_esquerda, coluna_meio, coluna_direita = st.columns([1, 1, 1])

setor = coluna_esquerda.selectbox("Setor", list(base["Setor"].unique()))
status = coluna_meio.selectbox("Status", list(base["Status"].unique()))

base = base[(base["Setor"] == setor) & (base["Status"] == status)]
base_mensal = (
    base.groupby(base["Data Chegada"].dt.to_period("M"))
    .sum(numeric_only=True)
    .reset_index()
)

base["Data Chegada"] = pd.to_datetime(
    base["Data Chegada"], dayfirst=True, errors="coerce"
)
base_mensal["Data Chegada"] = base_mensal["Data Chegada"].dt.to_timestamp()

container = st.container(border=True)

with container:
    # grafico de area
    st.write("Total de Projetos por mês (R$)")
    grafico_area = px.area(base_mensal, x="Data Chegada", y="Valor Negociado")
    st.plotly_chart(grafico_area)

    # grafico de colunas

    # titulo e filtro de ano
    coluna_esquerda, coluna_direita = st.columns([3, 1])
    coluna_esquerda.write("### Comparação Orçado x Pago")

    base_mensal["Ano"] = base_mensal["Data Chegada"].dt.year
    lista_anos = list(base_mensal["Ano"].unique())
    ano_selecionado = coluna_direita.selectbox("Ano", lista_anos)

    base_mensal = base_mensal[base_mensal["Ano"] == ano_selecionado]

    # metricas
    total_pago = base_mensal["Valor Negociado"].sum()
    total_desconto = base_mensal["Desconto Concedido"].sum()

    coluna_esquerda, coluna_direita = st.columns([1, 1])
    st.metric("Total Pago", f"R${total_pago:,}".replace(",", "."))
    st.metric("Total Deconto", f"R${total_desconto:,}".replace(",", "."))

    # grafico de barra
    grafico_barra = go.Figure(
        data=[
            go.Bar(
                name="Valor Orçado",
                x=base_mensal["Data Chegada"],
                y=base_mensal["Valor Orçado"],
                text=base_mensal["Valor Orçado"],
            ),
            go.Bar(
                name="Valor Pago",
                x=base_mensal["Data Chegada"],
                y=base_mensal["Valor Negociado"],
                text=base_mensal["Valor Negociado"],
            ),
        ]
    )

    grafico_barra.update_layout(barmode="group")
    st.plotly_chart(grafico_barra)
