import discord
from discord.ext import commands
from datetime import datetime


class ErrorHandling(commands.Cog, description="Handle the errors raised by the bot"):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, message):
        pass


def setup(client: commands.Bot):
    client.add_cog(ErrorHandling(client))
