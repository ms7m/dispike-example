import json
import uuid

from dispike import Dispike
from dispike.models import IncomingDiscordInteraction
from dispike.response import DiscordResponse
from dispike.register.models import DiscordCommand

bot = Dispike(**json.load(open("configuration.json", "r")))

command_configuration = DiscordCommand(
    name="secret", description="Generate a super secret key for your tools!", options=[]
)


@bot.interaction.on("secret")
async def handle_secret(ctx: IncomingDiscordInteraction) -> DiscordResponse:
    return DiscordResponse(
        content=f"""
        
        Hello {ctx.member.user.username}..
        
        Only you can see this message. **Do not share this key with anyone!**.

        Your key: || {uuid.uuid4()} ||

        """,
        empherical=True,
    )


if __name__ == "__main__":
    bot.register(command_configuration)
    bot.run()
