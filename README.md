# Desafio LuizaLabs

API Rest para gerenciar clientes e seus produtos favoritos

## Tecnologias utilizadas
* Python 3
* Flask
* MongoDB

## Getting Started

``git clone https://github.com/ylgnerbecton/api_luiza_labs.git``

# Pré-requisitos
* Python3
* MongoDB

# Instalação

pip3
* ``sudo apt-get install python3-pip``
* ``pip3 install virtualenv``

Pasta do projeto

``cd api_luiza_labs``

Ambiente virtual python

``python3 -m venv venv``

Verifique se você possui o MongoDB, se não tiver, [faça o download e instale na sua máquina](https://www.mongodb.com/download-center/community)


## Rodando a aplicação

Acesse a pasta raiz do projeto e entre no ambiente

``source venv/bin/activate``

Instale os requirements do projeto

``pip3 install -r requirements.txt``

Rodar projeto

``python3 run.py runserver``

## Rodando os testes

Comando para testar 

``python3 -m pytest``