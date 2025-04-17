import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())

@bot.command(name="hello", alias=["hi", "hey"])
async def hello_world(context):
    await context.send("Hello, world!")

if __name__ == "__main__":
    bot.run(TOKEN)