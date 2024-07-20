from micmic_api.auth.dao.join import MicmicJoinDAO
from micmic_api.auth.model.user import MicmicUserInfo


class MicmicJoinService:
    def __init__(self):
        self.dao = MicmicJoinDAO()

    def update_user_info(self, user_info: MicmicUserInfo):
        self.dao.save_user_info(user_info)
