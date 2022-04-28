# Copyright 2022 the author Rodney Sostras. All rights reserved.

import os
import click
import uvicorn

@click.group(help='Challenge Milenio Capital')
def execute_command_line():
    """
    Utilitario de linha de comando
    """
    pass

@click.command('runserver')
@click.option('--host', default='0.0.0.0', help="Listering on IP")
@click.option('--port', default=8080, help="Listering on Port")
def runserver(host, port):
    """
    Iniciar o serviço web de RestAPI
    """
    uvicorn.run("appconfig.core:application", host=host, port=port, reload=True)

execute_command_line.add_command(runserver)