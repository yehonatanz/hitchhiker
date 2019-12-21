from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Awaitable, Callable, List, Tuple, TypeVar

from telethon import TelegramClient, events

if TYPE_CHECKING:
    from .config import TelegramConfig

    ET = TypeVar("ET", bound=events.common.EventCommon)
    EventHandler = Callable[[ET], Awaitable[None]]

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARN
)


def create_client(config: TelegramConfig):
    return TelegramClient(config.app_name, config.api_id, config.api_hash)


@dataclass
class TelethonApp:
    handlers: List[Tuple[events.EventBuilder, EventHandler]] = field(
        default_factory=list
    )

    def on(self, event: events.EventBuilder) -> Callable[[EventHandler], EventHandler]:
        def _decorate(func: EventHandler) -> EventHandler:
            self.handlers.append((event, func))
            return func

        return _decorate

    def register(self, client: TelegramClient):
        for event, handler in self.handlers:
            client.add_event_handler(handler, event)
