import streamlit as st
from src.services.data_loader import carregar_dados
import plotly.express as px
from pathlib import Path

base = carregar_dados()


def criar_card(icone, numero, texto, coluna_card):
    container = coluna_card.container(border=True)
    coluna_esquerda, coluna_direita = container.columns([1, 2.5])
    coluna_esquerda.image(Path.cwd() / "assets" / "images" / f"{icone}", width=42)
    coluna_direita.write(numero)
    coluna_direita.write(texto)


coluna_esquerda, coluna_meio, coluna_direita = st.columns([1, 1, 1])

base_andamento = base[base["Status"] == "Em andamento"]
base_fechados = base[base["Status"].isin(["Em andamento", "Finalizado"])]


criar_card(
    "oportunidades.png",
    f"{(base['Código Projeto'].count()):,}".replace(",", "."),
    "Oportunidades",
    coluna_esquerda,
)
criar_card(
    "projetos_fechados.png",
    f"{(base_fechados['Código Projeto'].count()):,}".replace(",", "."),
    "Projetos Fechados",
    coluna_meio,
)
criar_card(
    "em_andamento.png",
    f"{(base_andamento['Código Projeto'].count()):,}".replace(",", "."),
    "Em Andamento",
    coluna_direita,
)

criar_card(
    "total_orcado.png",
    f"R${(base_fechados['Valor Orçado'].sum()):,}".replace(",", "."),
    "Total Orçado",
    coluna_esquerda,
)
criar_card(
    "total_pago.png",
    f"R${(base_fechados['Valor Negociado'].sum()):,}".replace(",", "."),
    "Total Pago",
    coluna_meio,
)
criar_card(
    "desconto.png",
    f"R${(base_fechados['Desconto Concedido'].sum()):,}".replace(",", "."),
    "Total Desconto",
    coluna_direita,
)

base_status = base.groupby("Status", as_index=False).count()
base_status = base_status.rename(columns={"Código Projeto": "Quantidade"})
base_status = base_status.sort_values(by="Quantidade", ascending=False)

grafico = px.funnel(base_status, x="Quantidade", y="Status")
st.plotly_chart(grafico)
