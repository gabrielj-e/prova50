# Projeto de Análise de Concordância (Django)

Este projeto é uma aplicação web construída com Django que modela, armazena e exibe regras de concordância verbal e nominal da língua portuguesa.

## 🚀 Funcionalidades

* **Modelagem de Dados:** O sistema utiliza 4 modelos principais:
    * `Regra`: Define as regras (ex: "Verbo concorda com sujeito").
    * `Nucleo`: Armazena os termos regentes (ex: "casa", "Eu").
    * `ElementoFlexionado`: Armazena os termos regidos (ex: "bonita", "corro").
    * `Mapeamento`: Conecta um Núcleo a um Elemento através de uma Regra, com uma frase de exemplo.
* **CRUD via Admin:** Gerenciamento completo dos dados através da interface de admin do Django.
* **Front-end Público:** Uma interface visual para navegar e visualizar os exemplos de concordância armazenados no banco de dados.

## 🤖 Tecnologias Utilizadas

* Python 3
* Django 4.x
* HTML5
* CSS3 (com layout básico)

* # Guia de Instalação

Siga os passos abaixo para rodar este projeto localmente.

## 1. Pré-requisitos

* Python 3.8+
* Git

## 2. Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    cd seu-repositorio
    ```

2.  **Crie e ative um Ambiente Virtual (Venv):**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate
    
    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    (Se você criou um `requirements.txt` com `pip freeze > requirements.txt`)
    ```bash
    pip install -r requirements.txt
    ```
    (Se não, instale o Django manualmente)
    ```bash
    pip install django
    ```

4.  **Aplique as Migrações:**
    Isso criará o banco de dados `db.sqlite3` com todas as tabelas.
    ```bash
    python manage.py migrate
    ```

5.  **Crie um Super Usuário:**
    Você precisará disso para acessar a área `/admin`.
    ```bash
    python manage.py createsuperuser
    ```

## 3. Rodando o Projeto

1.  **Inicie o servidor:**
    ```bash
    python manage.py runserver
    ```

2.  **Acesse a aplicação:**
    * **Site Público:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
    * **Área Admin:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## 4. (Opcional) Populando o Banco

Para ver dados de exemplo, acesse a área `/admin` e cadastre algumas `Regras`, `Nucleos` e `ElementosFlexionados`. Em seguida, crie `Mapeamentos` para conectar tudo.
