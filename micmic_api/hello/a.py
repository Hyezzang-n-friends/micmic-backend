from flask import jsonify, request, make_response
from flask_restx import Resource, Namespace

# app = Flask(__name__)
# api = Api(app=app)
hello_ns = Namespace('hello', description='Conference operations')


@hello_ns.route("/")
class HelloController(Resource):
    def get(self):
        """
            Edit9 returns a list of conferences
        """

        return make_response(jsonify({"status": "ok", "data": None}, 200))

    def post(self):
        """
            Adds a new conference to the list
        """
        body = request.get_json(force=True, silent=True)
        return make_response(jsonify({"status": "ok", "data": body}, 201))

    def put(self):
        """
            Displays a conference's details
        """
        return make_response(jsonify({"status": "ok", "data": None}), 200)

    def patch(self):
        """
            Edits a selected conference
        """
        return make_response(jsonify({"status": "ok", "data": None}), 200)

