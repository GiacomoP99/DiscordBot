from discord.ext.commands import Bot as BotBase
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord import Intents
from discord import Embed
from discord.ext.commands.errors import CommandNotFound
from ..db import db
from glob import glob


PREFIX = "!"
OWNER_IDS = [166164713653272578]
COGS = [path.split("\\")[-1][:-3] for path in glob("./lib/cogs/*.py")]


class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.guild = None
        self.scheduler = AsyncIOScheduler()
        self.ready = False
        db.autosave(self.scheduler)
        super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS, intents=Intents.all())

    def setup(self):
        for cog in COGS:
            self.load_extension(f"lib.cogs.{cog}")
            print(f"{cog} cog loaded")

        print("setup complete")

    def run(self, version):
        self.VERSION = version
        print("running setup...")
        self.setup()

        with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()
        print("running bot...")
        super().run(self.TOKEN, reconnect=True)

    async def print_message(self):
        await self.stdout.send("i'm a timed notification")

    async def on_connect(self):
        print("bot connected")

    async def on_disconnect(self):
        print("bot disconnected")

    async def on_error(self, err, *args, **kwargs):
        if err == "on_command_error":
            await args[0].send("Something went wrong.")
        raise err

    async def on_command_error(self, ctx, exc):
        if isinstance(exc, CommandNotFound):
            pass
        elif hasattr(exc, "original"):
            raise exc.original
        else:
            raise exc

    async def on_ready(self):
        if not self.ready:
            self.ready = True
            self.guild = self.get_guild(842067271664926730)
            self.scheduler.start()
            self.stdout = self.get_channel(842067271664926733)

            await self.stdout.send("Now online")
            # embed = Embed(title="Now online!",
            #               description="inconti let's ban ense", colour=0xFF0000)
            # fields = [("name", "value", True),
            #           ("another field", "this field is next to the other ", True),
            #           ("A non il line field", " this is not in line", False)]
            # for name, value, inline in fields:
            #     embed.add_field(name=name, value=value, inline=inline)
            # await channel.send(embed=embed)
            print("bot ready")
        else:
            print("bot reconnected")

    async def on_message(self, message):
        if not message.author.bot:
            await self.process_commands(message)


bot = Bot()
