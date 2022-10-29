import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv(dotenv_path="config")

default_intents = discord.Intents.default()
default_intents.message_content = True
default_intents.members = True

bot = commands.Bot(command_prefix="!", intents=default_intents)

@bot.event
async def on_ready():
    print("Le bot est prêt.")

@bot.event
async def on_message(message):
    if(message.content.lower() == "ping"):
        await message.channel.send("Pong")
        
    await bot.process_commands(message)

# tester avec josé
@bot.event
async def on_member_join(member):
    # : discord.TextChannel permet de spécifier le type de la variable, pas nécessaire, sert seulement pour l'autocomplétion
    general_channel: discord.TextChannel = bot.get_channel(695332959586091054)
    await general_channel.send(content=f"Bienvenue sur le serveur {member.display_name} !")

@bot.event
async def on_command_error(ctx, error):
    await ctx.channel.send(f"Cette commande n'existe pas, va te faire enculer :] (Erreur : {error})")

@bot.command(pass_context=True, name="del")
async def delete(ctx, number: int):
    if(number == ""):
        print("La variable est vide")
    messages = [message async for message in ctx.channel.history(limit=number+1)]

    for each_message in messages:
        await each_message.delete()

@bot.command(name="purge")
async def purge(ctx):
    await ctx.channel.purge()

@bot.command(name="moi")
async def moi(ctx):
    await ctx.channel.send(f"{ctx.me.mention} c'est moi wesh")

bot.run(os.getenv("TOKEN"))