from dispike.register.models import DiscordCommand
from dispike.response import DiscordResponse
from dispike.models import IncomingDiscordInteraction

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dispike import Dispike


command_configuration = DiscordCommand(
    name="secret", description="Generate a super secret key for your tools!", options=[]
)
