from __future__ import annotations

from typing import List, Optional

from telethon import events

from .config import HitchhikerConfig, TelegramConfig
from .telethon_utils import TelethonApp, create_client

config = HitchhikerConfig.load()
telegram_config = TelegramConfig.load()

app = TelethonApp()


def matcher(streets: Optional[List[str]]):
    if not streets:
        return lambda _: True
    return lambda message: any(street.lower() in message for street in streets)


@app.on(events.NewMessage(pattern=matcher(config.streets), chats=config.chats))
async def activete(event: events.NewMessage.Event):
    await event.reply("איתך")
    print(f"Hitchhiked: {event.message.raw_text}")
    if config.notify:
        print(f"Notifying {config.notify}")
        await event.client.send_message(
            config.notify, f"Hitchhiked a ride for you!\n{event.message.raw_text}"
        )
    await event.client.disconnect()


def main():
    client = create_client(telegram_config)
    app.register(client)

    print("Starting Hitchhiker")
    print(f"Config: {config}")
    with client.start(phone=telegram_config.phone):
        print("Running")
        client.run_until_disconnected()


if __name__ == "__main__":
    main()
