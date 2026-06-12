import streamlit as st
import pandas as pd
from pathlib import Path


@st.cache_data
def carregar_dados():
    tabela = pd.read_excel(Path.cwd() / "data" / "Base.xlsx")
    return tabela
