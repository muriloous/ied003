import streamlit as st
from pathlib import Path

DATA_FILE = Path("livros.txt")
GENEROS = ["Romance", "Ficção", "História", "Poesia"]

st.title("Cadastro de Livros")

with st.form("cadastro_livro"):
    titulo = st.text_input("Título do livro")
    autor = st.text_input("Autor")
    ano = st.number_input("Ano de publicação", min_value=0, max_value=2100, step=1, format="%d")
    genero = st.selectbox("Gênero literário", GENEROS)
    enviar = st.form_submit_button("Cadastrar livro")

if enviar:
    if not titulo.strip() or not autor.strip():
        st.error("Por favor, informe o título e o autor do livro.")
    else:
        print(DATA_FILE.parent)
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
        with DATA_FILE.open("a", encoding="utf-8") as arquivo:
            arquivo.write(f"{titulo.strip()}|{autor.strip()}|{ano}|{genero}\n")
        st.success("Livro cadastrado com sucesso!")

books = []
if DATA_FILE.exists():
    with DATA_FILE.open("r", encoding="utf-8") as arquivo:
        for line in arquivo:
            line = line.strip()
            if not line:
                continue
            parts = line.split("|")
            if len(parts) == 4:
                books.append({
                    "Título": parts[0],
                    "Autor": parts[1],
                    "Ano": parts[2],
                    "Gênero": parts[3],
                })

st.header("Livros cadastrados")
if books:
    st.table(books)
else:
    st.info("Nenhum livro cadastrado ainda.")

