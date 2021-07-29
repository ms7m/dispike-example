from dispike import Dispike
from .commands.forex import forex

bot = Dispike(...)

bot.register_collection(forex.ForexCommands(), register_command_with_discord=True)

if __name__ == "__main__":
    bot.run(port=5000)
