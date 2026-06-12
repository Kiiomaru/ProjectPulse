import streamlit as st
from pathlib import Path

caminho = Path.cwd()

sessao_usuario = st.session_state
nome_usuario = None
if "username" in sessao_usuario:
    nome_usuario = sessao_usuario.name

coluna_esquerda, coluna_direita = st.columns([1, 1.5])

if nome_usuario:
    st.title("Zênite")
    st.write(f"#### Bem vindo, {nome_usuario}")

botao_dashnoards = coluna_esquerda.button("Dashboards Projetos")
botao_indicadores = coluna_esquerda.button("Principais Indicadores")

if botao_dashnoards:
    st.switch_page(caminho / "views" / "dashboard.py")
if botao_indicadores:
    st.switch_page(caminho / "views" / "indicadores.py")

container = coluna_direita.container(border=True)
container.image(caminho / "assets" / "images" / "Zênite.png")
