from dispike import interactions
from dispike import DiscordCommand, PerCommandRegistrationSettings
from dispike.models.incoming import IncomingDiscordInteraction
from dispike.register.models import SubcommandOption, CommandTypes, CommandOption
import random
import httpx


class ForexCommands(interactions.EventCollection):
    def __init__(self):
        self._http_client = httpx.AsyncClient(headers={"Authorization": "..."})

    def return_stock_performance_bull(self, stock_name: str):
        return f"{stock_name} is up by {random.randint(0, 100)}%"

    async def return_portfolio_information(self, user_id: int):
        # Yeah, pretend you doing something here

        _get_information = await self._http_client.get(
            "https://stock-market.com", params={"userId": user_id}
        )
        percentage_change_amount = random.randint(0.1, 100)
        percentage_change = random.choice("% up", "% down")
        return f"{percentage_change_amount}{percentage_change}"

    async def return_gainers_today(self):
        _get_gainers = await self._http_client.get("https://stock-market.com")
        return random.choices(
            [
                self.return_stock_performance_bull("APPL"),
                self.return_stock_performance_bull("TSLA"),
                self.return_stock_performance_bull("GOOGL"),
                self.return_stock_performance_bull("F"),
                self.return_stock_performance_bull("FB"),
                self.return_stock_performance_bull("AAL"),
                self.return_stock_performance_bull("UTD"),
                self.return_stock_performance_bull("ACX"),
                self.return_stock_performance_bull("ABC"),
                self.return_stock_performance_bull("AAA"),
                self.return_stock_performance_bull("DIS"),
            ]
        )

    # DISCORD COMMANDS

    def commmand_schemas(self):
        return [
            DiscordCommand(
                name="bulls", description="Get the latest highest performing stocks."
            ),
            PerCommandRegistrationSettings(
                command=DiscordCommand(
                    id=None,
                    name="forex",
                    description="Get Forex rates",
                    options=[
                        SubcommandOption(
                            name="latest",
                            description="Get latest forex rates.",
                            type=2,
                            options=[
                                CommandOption(
                                    name="convert",
                                    description="View rates between two symbols.",
                                    type=1,
                                    required=False,
                                    options=[
                                        {
                                            "name": "symbol_1",
                                            "description": "Symbol 1",
                                            "type": CommandTypes.STRING,
                                            "required": True,
                                        },
                                        {
                                            "name": "symbol_2",
                                            "description": "Symbol 2",
                                            "type": CommandTypes.STRING,
                                            "required": False,
                                        },
                                    ],
                                )
                            ],
                        )
                    ],
                ),
                guild_id=11111,
            ),
        ]

    # EVENT CALLBACKS
    @interactions.on("forex.latest.convert")
    async def latest_conversion_for_forex(
        ctx: IncomingDiscordInteraction, symbol_1: str, symbol_2: str
    ):
        return f"{symbol_1} to {symbol_2} is {random.randint(0, 100)}"
