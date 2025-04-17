import random
from discord.ext import commands

class GamesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.hybrid_command(name="roll", description="Roll a dice")
    async def roll(self, ctx):
        result = random.randint(1, 6)
        await ctx.send(f"Résultat obtenu : {result}")
    
    @commands.hybrid_command(name="coinflip", description="Flip a coin")
    async def coinflip(self, ctx):
        result = random.choice(["pile", "face"])
        await ctx.send(f"Résultat obtenu : {result}")

async def setup(bot):
    await bot.add_cog(GamesCog(bot))
    print("Games cog loaded")