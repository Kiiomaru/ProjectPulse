from sqlalchemy.exc import IntegrityError
import re
import streamlit as st
from src.database.models import Usuario
from src.database.conection import session
import streamlit_authenticator as stauth
from pathlib import Path

st.title("Criar Conta")

form = st.form("form_criar_conta")
nome_usuario = form.text_input("Nome do usuário")
email_usuario = form.text_input("Email do usuário")
senha_usuario = form.text_input("Senha do Usuario", type="password")
admin_usuario = form.checkbox("É um admin?")
botao_submit = form.form_submit_button("Enviar")

if botao_submit:
    if not nome_usuario.strip():
        st.error("Digite um nome de usuario valido")

    elif not re.fullmatch(r"[\w.-]*@[\w.-]+\.[\w]{2,4}", email_usuario):
        st.error("Digite um email valido")

    elif len(senha_usuario) < 6:
        st.error("Senha deve conter mais que 6 caracteres")
    else:
        dados_provisorios = {"usernames": {"temporario": {"password": senha_usuario}}}
        stauth.Hasher.hash_passwords(dados_provisorios)  # type: ignore
        senha_criptografada = dados_provisorios["usernames"]["temporario"]["password"]
        usuario = Usuario(
            nome=nome_usuario,
            senha=senha_criptografada,
            email=email_usuario,
            admin=admin_usuario,
        )
        try:
            session.add(usuario)
            session.commit()
            st.success("Conta Criada com sucesso!")
            st.switch_page(Path.cwd() / "views" / "homepage.py")
        except IntegrityError:
            session.rollback()
            st.error("Esse email já está cadastrado")
