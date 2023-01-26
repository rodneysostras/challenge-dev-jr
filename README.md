```diff
! 🏳️ PROJETO IMPORTADO DO GITLAB - https://gitlab.com/rodneysostras/desafio-dev-jr-pl
```


<h1>
    <img src=".gitlab/assets/img/icon-readme-title.png" alt="" height="60em" align="left"/>
    Challenge Dev JR
</h1>
<div align="center">
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" />
    <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi&logoColor=white" />
</div>

<br />

<div align="center">
    <p>
        <a href="#-sobre-o-projeto">Sobre</a> •
        <a href="#-requisitos">Requisitos</a> •
        <a href="#-recursos">Recursos</a> •
        <a href="#-como-executar-o-projeto">Como executar</a> •
        <a href="#-tecnologias">Tecnologias</a> •
        <a href="#-autor">Autor</a>
    </p>
</div>

## 💻 Sobre o projeto

<br />

<div align="center"><img src=".gitlab/assets/img/icon-readme-body.png" alt="previewer" height="300em"/></div>

<div align="center">
    <em>
        Sistema de logística para definir melhores rotas entre cidades<br />
    </em>
</div>

<br />

🏆 Challenge Dev JR - Uma aplicação Web desenvolvida em python utilizando framework FastAPI.

Applicação tem objetivo de simplificar informando as melhores rotas entre algumas cidades para melhorar a logística de trabalho.

Sua base de dados persistente e o PostgreSQL um banco de dados relacional.

> Uma challenge realizada para testar meus conhecimentos tendo que comprir os requisitos abaixo.

> Branch da entrega '[challenge](https://github.com/rodneysostras/challenge-dev-jr/tree/challenge)'

<br />

## 🎯 Requisitos

> Os requisitos abaixo são resumidos, para melhores informações veja [documento oficial](docs/challenge.md)

- [X] API
  - [X] Criar | Esse endpoint deverá receber os dados e salvar no banco de dados.
  - [X] Recuperar | Esse endpoint deverá retornar um grafo previamente salvo no bando de dados.
  - [X] Calculo de distância | Esse endpoint deverá calcular todas as rotas disponíveis de uma cidade origem para outra de destino.
  - [X] Distância mínima | Esse endpoint deverá determinar a rota cuja distância seja a mínima possível entre duas cidades.
- [X] Dockerfile
- [X] Docker-compose com todos os serviços
- [ ] Testes de integração
- [ ] Documentação

<br />

## 📦 Recursos

- [X] Utilitario de linha de comando
- [X] Alembic - Ferramenta para gerenciar a estrutura do banco de dados
- [X] Collection Insomnia - Configuração para usar no software Isomnia

<br />

## 🚀 Como executar o projeto

```bash
# Clone este repositório
$ git clone https://gitlab.com/rodneysostras/desafio-dev-jr-pl.git
# Acesse a pasta do projeto no seu terminal/cmd
$ cd desafio-dev-jr-pl
# Acesse a pasta backend no seu terminal/cmd
$ cd backend
# Instalar as dependências
$ pip3 install -r requirements.txt
```

> Para executar o backend foi criado utilitario de linha de comando inspirado no Django, para usa-lo siga as instruções abaixo

```bash
# Criar ou atualizar as estruturas no banco de dados
$ python3 milenio.py migrate
# Iniciar serviço na porta padrão 8080
$ python3 milenio.py runserver
```

> Caso deseja utilizar da forma tradicional

```bash
# Criar ou atualizar as estruturas no banco de dados
$ alembic upgrade head
# Iniciar serviço na porta padrão 8080
$ uvicorn appconfig.core:application --host 0.0.0.0 --port 8080
```

> Na pasta `.devcontainer` possui as configurações para subir o container docker do ambiente de desenvolvimento deste projeto \
> Fique a vontade para usar o docker-composer ou a extensão do vscode `Remote Development` \
> Após o start do container realize o comando para; \
> \
> (1) - Instalação de dependências \
> (2) - Criação/atualização do banco de dados \
> (3) - Iniciar serviço \
> \
> Estes procedimentos estão descritos acima.

<br />

## 🛠 Tecnologias

-   **[Python](https://www.python.org/)** • Uma linguagem de programação de alto nível, é conhecida por usa simplicidade e legibilidade
-   **[FastAPI](https://fastapi.tiangolo.com/)** • Framework web para construções de APIs com Python 3.6 ou superior.
-   **[Postgresql](https://www.postgresql.org/)** • Sistema de banco de dados objeto-relacional de código aberto com mais de 30 anos de desenvolvimento

<br />

## 🦸 Autor

<table align="left">
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://github.com/rodneysostras.png" width="150px;" alt="Foto do Rodney Sostras no GitHub"/><br>
        <sub>
          <b>Rodney Sostras</b>
        </sub>
      </a>
    </td>
  </tr>
</table>
<p>
    &nbsp;&nbsp;
    <a href="https://github.com/rodneysostras">
        <img src="https://img.shields.io/badge/rodneysostras-000000?style=for-the-badge&logo=GitHub&logoColor=FFF" />
    </a>
</p>
<p>
    &nbsp;&nbsp;
    <a href="https://linkedin.com/in/rodney-sostras" alt="Linkedin do Rodney Sostras">
        <img src="https://img.shields.io/badge/-rodney--sostras-0077B5?style=for-the-badge&logo=Linkedin&logoColor=FFF"/>
    </a>
</p>
<p>&nbsp;&nbsp;
    <a href="mailto:rodney.sostras@gmail.com" alt="Email do Rodney Sostras">
        <img src="https://img.shields.io/badge/-rodney.sostras@gmail.com-D14836?style=for-the-badge&logo=Gmail&logoColor=FFF" />
    </a>
</p>
<p>&nbsp;&nbsp;
    <a href="https://rodneysostras.me/" alt="Web Site do Rodney Sostras">
        <img src="https://img.shields.io/badge/%F0%9F%8C%8E%20RODNEYSOSTRAS.ME%20-191919?style=for-the-badge" />
    </a>
</p>

<br />

<!-- ## 🎨 Creditos -->

<br />

## 📝 Licença

Este projeto esta sobe a licença [MIT](./LICENSE).

Feito com ❤️ por Rodney Sostras 👋🏽 [Entre em contato!](https://www.linkedin.com/in/rodney-sostras/)

<br />

<div align="right"><a href="#">Voltar ao topo ⬆</a></div>
