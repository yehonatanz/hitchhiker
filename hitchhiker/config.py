from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, ClassVar, Dict, List, Optional, Type, TypeVar, Union

TelegramIdentifier = Union[int, str]
PathLike = Union[str, Path]


class _ConfigMixin:
    DEFAULT_PATH: ClassVar[PathLike]

    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def from_dict(cls: Type[CT], data: Dict[str, Any]) -> CT:
        return cls(**data)

    @classmethod
    def load(cls: Type[CT], path: Optional[PathLike] = None) -> CT:
        with open(path or cls.DEFAULT_PATH, "r") as f:
            return cls.from_dict(json.load(f))


CT = TypeVar("CT", bound=_ConfigMixin)


@dataclass
class HitchhikerConfig(_ConfigMixin):
    DEFAULT_PATH = "hitchhiker.json"

    chats: List[TelegramIdentifier]
    streets: List[str]
    notify: Optional[TelegramIdentifier] = None


@dataclass
class TelegramConfig(_ConfigMixin):
    DEFAULT_PATH = "telegram.json"

    app_name: str
    api_id: int
    api_hash: str
    phone: str
