from flask import request, make_response
from flask_restx import Resource, fields

from common_lib.models.response import MicmicBaseResponse
from micmic_api.auth import auth_ns
from micmic_api.auth.model.join import MicmicJoinRequest
from micmic_api.auth.model.user import MicmicUserInfo
from micmic_api.auth.service.join import MicmicJoinService

join_request_model = auth_ns.model('MicmicJoinRequest', {
    'email': fields.String(required=True, description='User email address'),
    'name': fields.String(required=True, description='User name')
})


@auth_ns.route("/join")
class MicmicJoinController(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = MicmicJoinService()

    @auth_ns.expect(join_request_model)
    def post(self):
        body = request.get_json(force=True, silent=True)
        query = MicmicJoinRequest(**body)
        user_info = MicmicUserInfo(
            email=query.email,
            name=query.name
        )
        self.service.update_user_info(user_info)
        response = make_response(
            MicmicBaseResponse(data=None).to_dict(), 201
        )

        response.mimetype = "application/json"
        return response
