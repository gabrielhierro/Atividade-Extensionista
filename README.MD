<div align="center">
  <br>
  <img src="app_core/static/img/logo_nome.png" width="240" alt="Logo Pestalozzi de Maricá" style="margin-bottom:16px;"/>
  <p>
    <img alt="Tamanho do repositório" src="https://img.shields.io/github/repo-size/gabrielhierro/Atividade-Extensionista?color=F2E49B">
    <img alt="Último commit" src="https://img.shields.io/github/last-commit/gabrielhierro/Atividade-Extensionista?color=F2E49B">
    <img alt="Licença" src="https://img.shields.io/github/license/gabrielhierro/Atividade-Extensionista?color=F2E49B">
  </p>
  <br>
</div>

---

## 🌐 Acesse o Site

> [**Clique aqui para ver o projeto online**](https://gabrielhierro.pythonanywhere.com)

---

## 🧩 Sobre o Projeto

Este repositório reúne o código-fonte do novo site da **ONG Pestalozzi de Maricá**, desenvolvido como parte de um projeto extensionista com o objetivo de modernizar a presença digital da instituição.

A proposta vai além da aparência: buscamos tornar o site mais funcional, objetivo e alinhado às necessidades da ONG. Isso inclui reformular a estrutura de navegação, distribuir melhor o conteúdo e implementar um portal de comunicados interno.

---

## 🔍 Funcionalidades

- Página institucional com informações da ONG
- Aba de projetos com gerenciamento dinâmico pelo administrador (adicionar, editar e remover)
- Formulário de cadastro para novos voluntários
- Portal de comunicados com controle total pelo administrador
- Layout responsivo e organizado, com conteúdos distribuídos em páginas específicas

---

## 🛠️ Tecnologias Utilizadas

- ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white) **Python 3**
- ![Django](https://img.shields.io/badge/-Django-092E20?style=flat&logo=django&logoColor=white) **Django**
- ![SQLite](https://img.shields.io/badge/-SQLite-003B57?style=flat&logo=sqlite&logoColor=white) **SQLite**
- ![HTML5](https://img.shields.io/badge/-HTML5-E34F26?style=flat&logo=html5&logoColor=white) **HTML5**
- ![CSS3](https://img.shields.io/badge/-CSS3-1572B6?style=flat&logo=css3&logoColor=white) **CSS3**
- ![JavaScript](https://img.shields.io/badge/-JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black) **JavaScript**
- ![Bootstrap](https://img.shields.io/badge/-Bootstrap-7952B3?style=flat&logo=bootstrap&logoColor=white) **Bootstrap**
- ![Font Awesome](https://img.shields.io/badge/-Font%20Awesome-528DD7?style=flat&logo=fontawesome&logoColor=white) **Font Awesome**

---

## 🧪 Como rodar o projeto localmente

Siga os passos abaixo para rodar o projeto Django em sua máquina local:

```bash
# 1. Clone este repositório
git clone https://github.com/gabrielhierro/Atividade-Extensionista.git
cd Atividade-Extensionista

# 2. Crie um ambiente virtual
python -m venv venv

# 3. Ative o ambiente virtual
# No Windows:
venv\Scripts\activate

# No macOS/Linux:
source venv/bin/activate

# 4. Instale as dependências
pip install -r requirements.txt

# 5. Altere o modo de depuração
# No arquivo pestalozzi/settings.py, altere:
# DEBUG = False
# para:
# DEBUG = True

# 6. Aplique as migrações do banco de dados
python manage.py migrate

# 7. (Opcional) Crie um superusuário para acessar o admin
python manage.py createsuperuser

# 8. Rode o servidor de desenvolvimento
python manage.py runserver