import discord
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = discord.Client(intents=discord.Intents.all())

@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return
    if "quoi" in message.content.lower():
        await message.channel.send("FEUR")

bot.run(TOKEN)