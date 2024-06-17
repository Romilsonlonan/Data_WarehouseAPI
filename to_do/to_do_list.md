https://www.youtube.com/watch?v=-Pi5AmOfL2s&t=5431s

###################################### INSTALLATIONS ###################################### 

AMBIENTE FASTAPI: 

# Atualizar o sistema
sudo dnf update

# INSTALAÇÃO DO PYENV

# Instale dependência
sudo dnf install -y git gcc zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel tk-devel libffi-devel xz-devel

# Instale pyenv usando o script
curl https://pyenv.run | bash 

# Adicione as seguintes linhas ao seu arquivo de configuração de shell (~/.bashrc, `~/.zs~/.zshrc, etc)
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

# Adicione as seguintes linhas ao seu arquivo de configuração bash:
Comando:
nano .bashrc

Adicionar:

# Ambiente virtual para desenvolvimento com pyenv
```
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

```

# Após adicionar as linhas acima ao seu arquivo de configuração
source ~/.bashrc

#  Verifique quais as versões estão instaladas:
pyenv --version

# Alterar para uma outra versão:
pyenv global 3.9.19

# E para verificar se o pyenv-virtualenv está funcionando:
pyenv virtualenvs


# Instalar uma nova versão python 
pyenv update
pyenv install 3.12:latest

# Consultar as versões python instaladas 
pyenv install --list

# Instalar pipx
pip install pipx 

# Instalar as variáveis de sistema pipx
pipx ensurepath

Obs: Reiniciar o terminal 

# Instalar o poetry 
pipx install poetry

# Testar o poetry
poetry

# Instalar o ignr 
pipx install ignr 

# Instalar o gh para instalar o repositório e fazer alterações sem precisar acessar a pagina do github
verificar...

# Verificar pyproject.toml
cat pyproject.toml

# Instalar a versão local do projeto 
pyenv local 3.12.3

# Atualizar o arquivo [tool.poetry.dependencies] com .* para rodar com todas as versões
nano pyproject.toml
ex: [tool.poetry.dependencies]
    python = "^3.12" atualizar para python = "3.12.*"

# Certifique-se de que o Poetry está configurado para criar ambientes virtuais:
poetry config virtualenvs.in-project true

# Instalar o ambiente virtual 
poetry install 
poetry add fastapi

# Ative o ambiente virtual criado pelo Poetry
poetry shell

Obs: Toda vez que fechar o shell tem que rodar novamente o comando poetry shell

# Uvicorn é um servidor ASGI (Asynchronous Server Gateway Interface) de alto desempenho para Python, usado principalmente para executar aplicações web assíncronas. Ele é frequentemente utilizado com frameworks web modernos como FastAPI e Starlette, que são baseados em ASGI.
instalar:

pip install fastapi uvicorn

ou 

poetry add uvicorn

# Criar pasta e entrar:
mkdir fastapi_project
cd fastapi_project

# Executar a aplicação:
fastapi dev data_warehouseapi/app.py
fastapi run 

# Executar a aplicação em outras portas:
uvicorn data_warehouse.app:app --reload --port 8001
fastapi run data_warehouse/app.py --port 8001

# Criar um arquivo main.pycom o seguinte:
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


Executar um:

uvicorn main:app --reload

# O ruff pode ser usado para garantir que o código siga as convenções de estilo e padrões de qualidade, ajudando a detectar e corrigir problemas de formatação e possíveis bugs.
poetry add --group dev ruff 

# Configurando o ruff 
dentro do pyproject.toml add: 
[tool.ruff]
line-length = 79 
extend-exclude = ['migrations'] 

[tool.ruff.lint]
preview = true
select = ['I', 'F', 'E', 'W', 'PL', 'PT']

# Comando ruff para verificar o código:
ruff check . 

# Instalando o pytest: 
poetry add --group dev pytest pytest-cov

# Evitar bibliotecas externas 
[tool.pytest.ini_options]
pythonpath = "."
addopts = "-p no:warnings"

# Comando de análise pytestes 
pytest --cov=data_warehouse

# Comando pra criar um aliás:
[tool.taskipy.tasks]
run = 'fastapi dev data_warehouse/app.py'
pre_test = 'task lint'
test = 'pytest --cov=data_warehouse -vv'
post_test = 'coverage html'
lint = 'ruff check . ; ruff check . --diff'
format = 'ruff check . --fix ; ruff format .'

# Instalar taskpy:
poetry add --group dev taskipy

# Visualizar os comandos tasks 
task --list

# Jogando arquivos que não serão necessário para o gitignore 
ignr -p python > .gitignore

# Caso ainda apareça pastas persistentes executar os comando abaixo
ex: Primeiro, verifique se o seu .gitignore está configurado corretamente. Ele deve conter as linhas para ignorar os diretórios tests e to_do.

/tests/
/to_do/

git rm -r --cached tests/ to_do/
git add .gitignore
git commit -m "Atualiza .gitignore para excluir os diretórios tests e to_do"
git commit -m "Remove os diretórios tests e to_do do controle de versão"
git push origin main








