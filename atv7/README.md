# Cadastro de livros com Streamlit

Aplicação simples em Streamlit para cadastrar livros e salvar os dados em um arquivo `livros.txt`.

## Pré-requisitos

- Python3.11+

## Como rodar

1. Abra o terminal na pasta do projeto.

2. Configure o ambiente virtual (opcional).

      2.1. No primeiro uso, instale o ambiente virtual.

   ```bash
   python -m venv venv
   ```

      2.2. Ative o ambiente virtual.

   - PowerShell:
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```

   - Bash (Linux / macOS / Git Bash):
     ```bash
     source venv/bin/activate
     ```

3. Instale as dependências a partir do arquivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

5. Execute a aplicação:
   ```bash
   streamlit run streamlit_app.py
   ```

6. Acesse o link exibido no terminal para usar a aplicação.

## O que a aplicação faz

- Permite cadastrar um livro com título, autor, ano de publicação e gênero literário.
- Salva cada cadastro no final do arquivo `livros.txt`.
- Lê e exibe todos os livros cadastrados a cada novo envio.
