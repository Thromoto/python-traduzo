
# Projeto Traduzo

Uma ferramenta de tradução de textos entre vários idiomas, utilizando Python com o Framework Flask, para criar uma aplicação Server Side. Ou seja, o Backend irá fornecer a camada View, para a pessoa usuária.

Neste projeto:

* Implementar uma API utilizando arquitetura em camadas MVC;
* Utilizar o Docker para projetos Python;
* Aplicar conhecimentos de Orientação a Objetos no desenvolvimento WEB.
* Escrever testes para APIs para garantir a implementação dos endpoints;
* Interagir com um banco de dados não relacional MongoDB;
Desenvolver páginas web Server Side.


## Instalação

1. Clone o repositório.
```bash
git clone git@github.com:Thromoto/python-traduzo.git
```
2. Entre na pasta do repositório que você acabou de clonar.

3. Crie o ambiente virtual para o projeto.
```bash
python3 -m venv .venv && source .venv/bin/activate
```
4. Atualize seu pip antes de instalar as dependências.
```bash
python3 -m pip install --upgrade pip
```
5. Instale as dependências.
```bash
python3 -m pip install -r dev-requirements.txt
```
6. Suba o projeto pelo Docker.
```bash
docker compose up translate
```
7. Para popular o banco de dados com as seeds que estão prontas com mais de 130 idiomas, basta executar em um terminal paralelo.
```bash
docker compose exec -it translate python3 src/run_seeds.py
```
8. Para acessar a aplicação pelo navegador `http://127.0.0.1:8000/`.


## Stack utilizada

Python, Framework Flask, MVC, Docker, MongoDB, POO.