from flask import Flask
from flask_restx import Api

from common_lib.infra.mysql import MySQLConnection
from micmic_api import config


def create_app():
    app = Flask(__name__)
    # app.config["PROPAGATE_EXCEPTIONS"] = True
    # app.config.from_object(config)가

    api = Api(app=app)
    register_namespaces(api)
    initialize()
    return app


def register_namespaces(api: Api) -> None:
    from micmic_api.hello.a import hello_ns
    from micmic_api.auth.a import auth_ns
    ns_confs = [hello_ns, auth_ns]
    for ns_conf in ns_confs:
        api.add_namespace(ns_conf)


def initialize():
    db = MySQLConnection(
        stage=config.STAGE,
        ssh_host=config.SSH_HOST,
        ssh_port=config.SSH_PORT,
        ssh_user=config.SSH_USER,
        ssh_pkey=config.SSH_KEY,
        db_user=config.MYSQL_USER,
        db_password=config.MYSQL_PASSWORD,
        db_name=config.MYSQL_DB,
        db_host=config.MYSQL_HOST,
        db_port=config.MYSQL_PORT,
    )
    conn = db.connect()
    cursor = conn.cursor()
    sql = """
        SELECT * FROM users;
    """
    cursor.execute(sql)
    row = cursor.fetchone()
    print(row)

    conn.close()
