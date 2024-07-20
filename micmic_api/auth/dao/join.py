from common_lib.infra.mysql import MySQLConnection
from micmic_api import config
from micmic_api.auth.model.user import MicmicUserInfo


class MicmicJoinDAO:
    def __init__(self):
        self.db = db = MySQLConnection(
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
        self.cursor = db.connect().cursor()

    def save_user_info(self, user_info: MicmicUserInfo) -> None:
        sql = f"""
            INSERT 
                INTO USERS (NAME, EMAIL)
            VALUES 
                (%(name)s, %(email)s);
        """
        self.cursor.execute(sql, {
            "name": user_info.name,
            "email": user_info.email
        })
