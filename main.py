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

    await ctx.channel.send(f"{number} message(s) ont été supprimés", delete_after=2)

# @bot.command(name="purge")
# async def purge(ctx):
#     await ctx.channel.purge()

@bot.command(name="moi")
async def moi(ctx):
    await ctx.channel.send(f"{ctx.me.mention} c'est moi wesh")

@bot.command(name="salut")
async def salut(ctx):
    await ctx.channel.send("Wesh poto")

@bot.command(name="serverinfo")
async def serverInfo(ctx):
    server = ctx.guild
    serverName = server.name
    serverOwner = server.owner
    numberOfTextChannels = len(server.text_channels)
    numberOfVocalChannels = len(server.voice_channels)
    descriptionServer = server.description
    numberOfMembers = server.member_count

    # revoir ici, fonctionne mal
    numberofConnectedMembers = 0
    for member in server.members:
        if member.status is not discord.Status.offline:
            numberofConnectedMembers+=1
    
    # pas utilisé, ne rend pas très bien
    image = server.icon

    messageInfo = f"Le serveur **{serverName}** contient {numberOfMembers} membres dont {numberofConnectedMembers} connectés.\nIl appartient à {serverOwner}\nLa description du serveur est : {descriptionServer}\nCe serveur possède {numberOfTextChannels} salons textuels et {numberOfVocalChannels} salons vocaux."

    await ctx.channel.send(messageInfo)

@bot.command(name="say")
async def say(ctx, *phrase):
    await ctx.channel.send(" ".join(phrase))

@bot.command(name="says")
async def says(ctx, number : int, *phrase):
    for i in range(number):
        await ctx.channel.send(" ".join(phrase))

@bot.command(name="getinfo")
async def getinfo(ctx, infoDemandee):
    reponse = True

    if infoDemandee == "memberCount":
        await ctx.channel.send(f"Ce serveur contient {ctx.guild.member_count} membres.") 
    elif infoDemandee == "numberOfChannel":
        await ctx.channel.send(f"Ce serveur contient {len(ctx.guild.text_channels) + len(ctx.guild.voice_channels)} salons (textuels ou vocaux).") 
    elif infoDemandee == "name":
        await ctx.channel.send(f"Ce serveur s'appelle **{ctx.guild.name}**.") 
    else:
        reponse = False
    
    if not(reponse):
        await ctx.channel.send("Le paramètre entré n'est pas bon.\nLes paramètres disponibles sont : memberCount, numberOfChannel et name.")       


bot.run(os.getenv("TOKEN"))