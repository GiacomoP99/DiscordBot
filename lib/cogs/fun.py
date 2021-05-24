from discord.ext.commands import Cog
from discord.ext.commands import command
from random import randint
from discord.utils import get
from discord import Embed


class Fun(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.TeamList = self.getdata()

    def storedata(self):
        f = open("./data/listateam.txt", "w")
        for word in self.TeamList:
            stringa = str(word) + "\n"
            f.write(stringa)
            for parole in self.TeamList[word]:
                stringa = str(parole) + "\n"
                f.write(stringa)
        f.close()

    def getdata(self):
        f = open("./data/listateam.txt", "r")
        lista = f.read()
        lista = lista.replace("\n", " ").split(" ")
        currentteam = ""
        listateam = {}
        first = True
        for word in lista:
            if len(word) < 2:
                continue
            else:
                if "team".upper() in word:
                    currentteam = word
                    first = True
                else:
                    if first:
                        listateam.update({str(currentteam): [str(word)]})
                        first = False
                    else:
                        listateam[str(currentteam)].append(str(word))
        f.close()
        return listateam

    @command(name="hello")
    async def say_hello(self, ctx):
        print(self.TeamList)
        await ctx.send(f"Hello {ctx.author.mention}!")

    @command(name="addme")
    async def add_me(self, ctx):
        sender = ctx.message.author
        content = ctx.message.content.replace("!addme ", "")
        self.TeamList[str(content).upper()].append(str(sender))
        self.storedata()
        await ctx.send("added with success!")

    @command(name="createam")
    async def crea_team(self, ctx):
        sender = ctx.message.author
        content = ctx.message.content.replace("!createam ", "")
        self.TeamList.update({str(content).upper(): [str(sender)]})
        self.storedata()
        await ctx.send("added with success!")

    @command(name="teamlist")
    async def team_list(self, ctx):
        res = ""
        for word in self.TeamList:
            stringa = str(word).upper() + "\n"
            await ctx.send(stringa)
            for parole in self.TeamList[word]:
                res += str(parole) + ", "
            await ctx.send(res)
            res = ""

    @command(name="flame")
    async def flame_marco(self, ctx):
        member = get(self.bot.get_all_members(), id=717697262221918210)
        insulti = ["puzzi", "zitto!", "vai a fare cali", "vergogna"]
        await ctx.send(f"{member.mention} {insulti[randint(0,3)]}")

    @command(name="newbt")
    async def add_new_bt(self, ctx):
        content = ctx.message.content.replace("!newbt ", "").split(" ")
        await ctx.message.delete()
        embed = Embed(title="NUOVA BOUNTY TRIALS",
                      description=f"bounty trials di {content[0]}", colour=0xFF0000)
        embed.set_image(
            url=str(content[1]))
        await ctx.send(embed=embed)

    @command(name="beer")
    async def cheers(self, ctx):
        content = ctx.message.content.replace("!beer ", "").split(" ")
        sender = ctx.message.author
        embed = Embed(
            title=f"{sender} e {content[0]} brindano con una bella birra!")
        embed.set_image(
            url="https://media.giphy.com/media/Ig3XsprShY8TGoutIE/giphy.gif")
        await ctx.send(embed=embed)

    @command(name="pain")
    async def pain_meme(self, ctx):
        embed = Embed()
        embed.set_image(
            url="https://i.postimg.cc/vB06NktY/vayc9gwh93051.jpg")
        await ctx.send(embed=embed)

    @command(name="newv")
    async def add_new_voyage(self, ctx):
        content = ctx.message.content.replace("!newv ", "").split(" ")
        await ctx.message.delete()
        embed = Embed(title="NUOVA VIAGGIO DELLE MERAVIGLIE", colour=0xFF0000)
        embed.set_image(
            url=str(content[0]))
        await ctx.send(embed=embed)

    @command(name="newm")
    async def add_new_mongolfiera(self, ctx):
        content = ctx.message.content.replace("!newm ", "").split(" ")
        await ctx.message.delete()
        embed = Embed(title="NUOVA MONGOLFIERA ITINERANTE", colour=0xFF0000)
        embed.set_image(
            url=str(content[0]))
        await ctx.send(embed=embed)

    @command(name="newpatch")
    async def add_new_patch(self, ctx):
        content = ctx.message.content.replace("!newpatch ", "").split(" ")
        await ctx.message.delete()
        embed = Embed(title="NUOVA PATCH " + f"{content[0]}", colour=0xFF0000)
        content.pop(0)
        embed.set_image(
            url=str(content[0]))
        content.pop(0)
        await ctx.send(embed=embed)
        for link in content:
            embed = Embed(colour=0xFF0000)
            embed.set_image(
                url=str(link))
            await ctx.send(embed=embed)

    @command(name="newhero")
    async def add_new_hero(self, ctx):
        content = ctx.message.content.replace("!newhero ", "").split(" ")
        await ctx.message.delete()
        embed = Embed(title="NUOVO EROE " + f"{content[0]}", colour=0xFF0000)
        content.pop(0)
        embed.set_image(
            url=str(content[0]))
        content.pop(0)
        await ctx.send(embed=embed)
        for link in content:
            embed = Embed(colour=0xFF0000)
            embed.set_image(
                url=str(link))
            await ctx.send(embed=embed)

    @command(name="newhspo")
    async def add_new_spoiler(self, ctx):
        content = ctx.message.content.replace("!newhspo ", "").split(" ")
        await ctx.message.delete()
        url = content[len(content) - 1]
        content.pop(len(content) - 1)
        title = content[0]
        content.pop(0)
        embed = Embed(title="NUOVO EROE " +
                      f"{title}", description=' '.join([str(elem) for elem in content]), colour=0xFF0000)
        embed.set_image(
            url=str(url))
        content.pop(0)
        await ctx.send(embed=embed)

    @Cog.listener()
    async def on_ready(self):
        print("fun cog ready")


def setup(bot):
    bot.add_cog(Fun(bot))
