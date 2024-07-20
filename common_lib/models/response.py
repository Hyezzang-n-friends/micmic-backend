from dataclasses import dataclass
from typing import Optional, Any

from dataclasses_json import DataClassJsonMixin


@dataclass
class MicmicBaseResponse(DataClassJsonMixin):
    data: Optional[Any]


@dataclass
class MicmicError(DataClassJsonMixin):
    message: str


@dataclass
class MicmicErrorResponse(MicmicBaseResponse):
    error: MicmicError
