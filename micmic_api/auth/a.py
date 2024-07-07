from flask import jsonify, request, make_response
from flask_restx import Resource, Namespace

# app = Flask(__name__)
# api = Api(app=app)
auth_ns = Namespace('auth', description='Auth API')


@auth_ns.route("/")
class AuthController(Resource):
    def get(self):
        """
            Auth Get
        """

        return make_response(jsonify({"status": "ok", "data": None}, 200))

    def post(self):
        """
            Auth Post
        """
        body = request.get_json(force=True, silent=True)
        return make_response(jsonify({"status": "ok", "data": body}, 201))

    def put(self):
        """
            Auth Put
        """
        return make_response(jsonify({"status": "ok", "data": None}), 200)

    def patch(self):
        """
            Auth Patch
        """
        return make_response(jsonify({"status": "ok", "data": None}), 200)
