import json
import uuid

import httpx
from dispike import Dispike
from dispike.models import IncomingDiscordInteraction
from dispike.response import DiscordResponse

from .commands.latest_rates import command_configuration as latest_rates_configuration
from .commands.secret_code import command_configuration as secret_code_configuration

bot = Dispike(**json.load(open("configuration.json", "r")))


commands_to_configure = [latest_rates_configuration, secret_code_configuration]

for command in commands_to_configure:
    bot.register(command)


@bot.interaction.on("secret")
async def handle_secret(*args, **kwargs) -> DiscordResponse:
    return DiscordResponse(
        content=f"""
        Only you can see this message. **Do not share this key with anyone!**.

        Your key: || {uuid.uuid4()} ||

        """,
        empherical=True,
    )


@bot.interaction.on("forex.latest.convert")
async def handle_forex_conversion_rates(
    symbol_1: str, symbol_2: str, ctx: IncomingDiscordInteraction
) -> DiscordResponse:
    async with httpx.AsyncClient() as client:
        try:
            _send_request = await client.get(
                f"https://api.ratesapi.io/api/latest?base={symbol_1.upper()}&symbols={symbol_2.upper()}"
            )
            if _send_request.status_code == 400:
                return DiscordResponse(
                    content=f"Unable to find that forex due to an error: {_send_request.json()['error']}"
                )
            elif _send_request.status_code == 200:
                _parse_request = _send_request.json()
                return DiscordResponse(
                    content=f"1 {symbol_1.upper()} ~= {_parse_request['rates'][symbol_2.upper()]} {symbol_2.upper()}",
                    show_user_input=True,
                )
            else:
                return DiscordResponse(
                    content=f"There was an issue contacting the Forex API. {_send_request.status_code}",
                    empherical=True,
                )
        except Exception:
            return DiscordResponse(
                content="There was an issue with our bot. Try again later."
            )


if __name__ == "__main__":
    bot.run()
