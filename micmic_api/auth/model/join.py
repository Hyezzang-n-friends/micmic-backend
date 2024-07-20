from dataclasses import dataclass

from dataclasses_json import DataClassJsonMixin


@dataclass
class MicmicJoinRequest(DataClassJsonMixin):
    email: str
    name: str
