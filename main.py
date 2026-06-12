import streamlit as st
import streamlit_authenticator as stauth
from src.database.models import Usuario
from src.database.conection import session
from pathlib import Path


lista_usuarios = session.query(Usuario).all()

credenciais = {
    "usernames": {
        usuario.email: {"name": usuario.nome, "password": usuario.senha}
        for usuario in lista_usuarios
    }
}

authenticator = stauth.Authenticate(
    credenciais,
    "credenciais_Zênite",
    "jsahcsihioahdcacgcucuoGxajncuehf",
    cookie_expiry_days=30,
)


def autenticar_usuario(authenticator):
    authenticator.login()
    status_autenticacao = st.session_state.get("authentication_status")
    nome = st.session_state.get("name")
    username = st.session_state.get("username")
    if status_autenticacao:
        return {"nome": nome, "username": username}
    elif status_autenticacao is False:
        st.error("Combinação de úsuario e senha inválidas")
    else:
        st.error("Preencha o formulário para fazer login")


def logout():
    authenticator.logout()


# autenticar usuario
dados_usuario = autenticar_usuario(authenticator)
caminho = Path.cwd()

if dados_usuario:
    email_usuario = dados_usuario["username"]
    usuario = session.query(Usuario).filter_by(email=email_usuario).first()

    if usuario.admin:  # type: ignore
        pg = st.navigation(
            {  # type: ignore
                "Home": [st.Page(caminho / "views" / "homepage.py", title="Zênite")],
                "Dashboards": [
                    st.Page(caminho / "views" / "dashboard.py", title="DashBoard"),
                    st.Page(caminho / "views" / "indicadores.py", title="Indicadores"),
                ],
                "Conta": [
                    st.Page(
                        caminho / "src" / "auth" / "criar_conta.py",
                        title="Criar Conta",
                    ),
                    st.Page(logout, title="Sair"),
                ],
            }
        )
    else:
        pg = st.navigation(
            {  # type: ignore
                "Home": [st.Page(caminho / "views" / "homepage.py", title="Zênite")],
                "Dashboards": [
                    st.Page(caminho / "views" / "dashboard.py", title="DashBoard"),
                    st.Page(caminho / "views" / "indicadores.py", title="Indicadores"),
                ],
                "Conta": [
                    st.Page(logout, title="Sair"),
                ],
            }
        )
    pg.run()
