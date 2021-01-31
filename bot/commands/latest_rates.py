from dispike.register.models import DiscordCommand
from dispike.register.models.options import (
    CommandOption,
    CommandTypes,
    SubcommandOption,
)
from dispike.response import DiscordResponse
from dispike.models import IncomingDiscordInteraction

import httpx


command_configuration = DiscordCommand(
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
)