import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

class MyBot(commands.Bot):
    async def setup_hook(self):
        for extension in ['games']:
            await self.load_extension(f"cogs.{extension}")

intents = discord.Intents.all()
bot = MyBot(command_prefix="$", intents=intents)

def main():
    bot.run(TOKEN)

if __name__ == "__main__":
    main()