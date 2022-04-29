# Copyright 2022 the author Rodney Sostras. All rights reserved.

## Management
## Recursos necessário para criação da CLI

import os
import click
import uvicorn

# CLI
@click.group(help='Challenge Milenio Capital')
def execute_command_line():
    """ Utilitario de linha de comando """
    pass

# Runserver
@click.command('runserver')
@click.option('--host', default='0.0.0.0', help="Listering on IP")
@click.option('--port', default=8080, help="Listering on Port")
def runserver(host, port):
    """ Iniciar o serviço web de RestAPI """
    uvicorn.run("appconfig.core:application", host=host, port=port, reload=True)

execute_command_line.add_command(runserver)

# Database Make Migration
@click.command('makemigration')
def makemigration():
    """ Gera o arquivo de estrutura do banco de dados """
    os.system('alembic revision --autogenerate')

execute_command_line.add_command(makemigration)

# Database migrate
@click.command('migrate')
def migrate():
    """ Cria ou atualiza a estrutura no banco de dados """
    os.system('alembic upgrade head')

execute_command_line.add_command(migrate)