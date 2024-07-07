from flask import Flask
from flask_restx import Api


def create_app():
    app = Flask(__name__)
    api = Api(app=app)
    register_namespaces(api)
    return app


def register_namespaces(api: Api) -> None:
    from micmic_api.hello.a import hello_ns
    from micmic_api.auth.a import auth_ns
    ns_confs = [hello_ns, auth_ns]
    for ns_conf in ns_confs:
        api.add_namespace(ns_conf)
