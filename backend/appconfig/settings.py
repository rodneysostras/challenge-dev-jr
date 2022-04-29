# Copyright 2022 the author Rodney Sostras. All rights reserved.

## Settings
## Possui informações de configuração
## necessária para funcionamento do serviço

import os
from pathlib import Path
from os.path import join
from dotenv import load_dotenv

from appconfig.exception import ConfigException

# Utilitario que especifica o caminho da raiz do diretório backend 
BASE_DIR = Path(__file__).resolve().parent.parent

# Recurso para carregar variaveis do arquivo .env na raiz do diretório backend
dotenv_path = join(BASE_DIR, '.env')
load_dotenv(dotenv_path)

# Database
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL: raise ConfigException("DATABASE_URL is None")