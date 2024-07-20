from dataclasses import dataclass

from dataclasses_json import DataClassJsonMixin


@dataclass
class MicmicUserInfo(DataClassJsonMixin):
    email: str
    name: str
