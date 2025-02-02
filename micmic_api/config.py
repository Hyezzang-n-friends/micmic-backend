import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../", ".env")
load_dotenv(dotenv_path)

STAGE = os.getenv("STAGE")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = int(os.getenv("MYSQL_PORT", "3306"))
MYSQL_DB = os.getenv("MYSQL_DB")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
SSH_HOST = os.getenv("SSH_HOST")
SSH_PORT = int(os.getenv("SSH_PORT"))
SSH_USER = os.getenv("SSH_USER")
SSH_KEY = os.path.join(os.path.dirname(__file__), "../keys/micmic-backend.pem")
