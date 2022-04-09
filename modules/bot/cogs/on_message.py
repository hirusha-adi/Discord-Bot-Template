import discord
from discord.ext import commands

from bot.database.manager import blacklisted
from bot.database.manager import main


class OnMessage(commands.Cog, description="Handle the errors raised by the bot"):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, message):

        if self.client.user == message.author:
            return

        if message.author.id in blacklisted.blacklisted_users_all_lines:
            if str(message.content).startswith(main.prefix):
                await message.reply('You are blacklisted from usin this bot!')
                return


def setup(client: commands.Bot):
    client.add_cog(OnMessage(client))
