from flask import Flask, jsonify, request, make_response
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app=app)
ns_conf = api.namespace('hello', description='Conference operations')


@ns_conf.route("/")
class HelloController(Resource):
    def get(self):
        """
            returns a list of conferences
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=7890)
