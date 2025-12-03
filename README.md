# 🎬 Movie Review API

API RESTful desenvolvida em **Django** e **Django REST Framework** para gerenciamento de filmes, atores, gêneros e reviews.  
A autenticação é feita por **JSON Web Tokens (JWT)**, garantindo segurança e controle de acesso.

---

## 🚀 Funcionalidades

- 🔐 **Autenticação JWT** (login e refresh de tokens)  
- 🎞️ **CRUD completo de filmes**  
- 🧑‍🎤 **Cadastro e listagem de atores**  
- 🏷️ **Gerenciamento de gêneros**  
- 📝 **Criação e visualização de reviews de filmes**  
- ⚙️ **Padrão RESTful** com versionamento de API (`/api/v1/...`)

---

## 🧩 Estrutura dos Endpoints

### 🔐 Autenticação
| Método | Endpoint | Descrição |
|--------|-----------|-----------|
| `POST` | `/api/v1/authentication/token/` | Gera um token JWT (login) |
| `POST` | `/api/v1/authentication/token/refresh/` | Atualiza o token JWT |

### 🎞️ Filmes
| Método | Endpoint | Descrição |
|--------|-----------|-----------|
| `GET` | `/api/v1/movies/` | Lista todos os filmes |
| `POST` | `/api/v1/movies/` | Cria um novo filme |
| `GET` | `/api/v1/movies/{id}/` | Detalhes de um filme |
| `PUT` | `/api/v1/movies/{id}/` | Atualiza um filme |
| `DELETE` | `/api/v1/movies/{id}/` | Exclui um filme |

### 🧑‍🎤 Atores
| Método | Endpoint | Descrição |
|--------|-----------|-----------|
| `GET` | `/api/v1/actors/` | Lista todos os atores |
| `POST` | `/api/v1/actors/` | Cadastra um novo ator |
| `GET` | `/api/v1/actors/{id}/` | Detalhes de um ator |
| `PUT` | `/api/v1/actors/{id}/` | Atualiza um ator |
| `DELETE` | `/api/v1/actors/{id}/` | Exclui um ator |

### 🏷️ Gêneros
| Método | Endpoint | Descrição |
|--------|-----------|-----------|
| `GET` | `/api/v1/genres/` | Lista todos os gêneros |
| `POST` | `/api/v1/genres/` | Cria um novo gênero |
| `GET` | `/api/v1/genres/{id}/` | Detalhes de um gênero |
| `PUT` | `/api/v1/genres/{id}/` | Atualiza um gênero |
| `DELETE` | `/api/v1/genres/{id}/` | Exclui um gênero |

### 📝 Reviews
| Método | Endpoint | Descrição |
|--------|-----------|-----------|
| `GET` | `/api/v1/reviews/` | Lista todas as reviews |
| `POST` | `/api/v1/reviews/` | Cria uma nova review |
| `GET` | `/api/v1/reviews/{id}/` | Detalhes de uma review |
| `PUT` | `/api/v1/reviews/{id}/` | Atualiza uma review |
| `DELETE` | `/api/v1/reviews/{id}/` | Exclui uma review |

---

## ⚙️ Tecnologias Utilizadas

- [Python 3.x](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- [SQLite / PostgreSQL](https://www.postgresql.org/) (dependendo do ambiente)

---

## 🏗️ Instalação e Execução

```bash
# 1️⃣ Clonar o repositório
git clone https://github.com/usuario/movie-review-api.git
cd movie-review-api

# 2️⃣ Criar e ativar o ambiente virtual
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

# 3️⃣ Instalar dependências
pip install -r requirements.txt

# 4️⃣ Executar migrações
python manage.py migrate

# 5️⃣ Rodar o servidor
python manage.py runserver
