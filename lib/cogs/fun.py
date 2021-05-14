from discord.ext.commands import Cog
from discord.ext.commands import command
from random import randint
from discord.utils import get


class Fun(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="hello")
    async def say_hello(self, ctx):
        await ctx.send(f"Hello {ctx.author.mention}!")

    @command(name="flame")
    async def flame_marco(self, ctx):
        member = get(self.bot.get_all_members(), id=299989967659335691)
        insulti = ["puzzi", "zitto!", "vai a fare cali", "vergogna"]
        await ctx.send(f"{member.mention} {insulti[randint(0,3)]}")

    @Cog.listener()
    async def on_ready(self):
        print("fun cog ready")


def setup(bot):
    bot.add_cog(Fun(bot))
