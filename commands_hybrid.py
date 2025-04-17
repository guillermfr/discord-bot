import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())

@bot.hybrid_command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.hybrid_command()
async def soustraire(ctx, a: int, b: int):
    await ctx.send(f"{a} - {b} = {a - b}")

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)} commandes synchronisées")
    except Exception as e:
        print(e)

def main():
    bot.run(TOKEN)

if __name__ == "__main__":
    main()