import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())

@bot.tree.command()
async def multiplication(interaction: discord.Interaction, a: int, b: int):
    await interaction.response.send_message(f"{a} * {b} = {a * b}")

@bot.tree.command()
async def repeat_message(interaction : discord.Interaction, nombre: int, message: str):
    await interaction.response.send_message(message)
    for _ in range(1, nombre):
        await interaction.followup.send(message)

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)} commandes synchronisées")
    except Exception as e:
        print(e)

bot.run(TOKEN)