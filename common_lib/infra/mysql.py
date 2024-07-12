import mysql.connector
from mysql.connector import Error
from sshtunnel import SSHTunnelForwarder

from common_lib.utils.singleton import Singleton


class MySQLConnection(Singleton):
    def __init__(self, stage: str, ssh_host: str, ssh_port: str, ssh_user: str, ssh_pkey: str, db_user: str,
                 db_password: str,
                 db_name: str, db_host: str, db_port: str):
        if not hasattr(self, 'initialized'):
            self.stage = stage
            self.ssh_host = ssh_host
            self.ssh_port = ssh_port
            self.ssh_user = ssh_user
            self.ssh_pkey = ssh_pkey
            self.db_user = db_user
            self.db_password = db_password
            self.db_name = db_name
            self.db_host = db_host
            self.db_port = db_port
            self.ssh_tunnel = None
            self.db_connection = None
            self.initialized = True  # 초기화 플래그 설정

    def connect(self):
        try:
            if self.stage == "dev" and self.ssh_tunnel is None:
                self.ssh_tunnel = SSHTunnelForwarder(
                    (self.ssh_host, self.ssh_port),
                    ssh_username=self.ssh_user,
                    ssh_pkey=self.ssh_pkey,
                    remote_bind_address=(self.db_host, self.db_port),
                )
                self.ssh_tunnel.start()
                print("ssh_tunnel_connected")

            if self.stage == "dev":
                self.db_port = self.ssh_tunnel.local_bind_port
            if self.db_connection is None:
                self.db_connection = mysql.connector.connect(
                    host=self.db_host,
                    port=self.db_port,
                    user=self.db_user,
                    password=self.db_password,
                    database=self.db_name,
                    use_pure=True
                )
                self.db_connection.autocommit = True
                print("mysql_connected")
            return self.db_connection
        except Error as e:
            print("Error while connecting to MySQL", e)

    def close(self):
        if self.db_connection:
            self.db_connection.close()
            self.db_connection = None
        if self.ssh_tunnel:
            self.ssh_tunnel.stop()
            self.ssh_tunnel = None
        print("MySQL connection is closed")
