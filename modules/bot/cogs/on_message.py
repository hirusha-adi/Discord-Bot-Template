import discord
from discord.ext import commands

from bot.database.manager import blacklisted
from bot.database.manager import main


class OnMessage(commands.Cog, description="Handle the messages sent"):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, message: discord.Message):

        if self.client.user == message.author:
            return

        if message.guild.id in blacklisted.blacklisted_guilds_all_lines:
            if str(message.content).startswith(main.prefix):
                await message.reply('This server is blacklisted by the admins')
                return

        if message.author.id in blacklisted.blacklisted_users_all_lines:
            if str(message.content).startswith(main.prefix):
                await message.reply('You are blacklisted from using this bot!')
                return

        if self.client.user.mentioned_in(message):
            await message.reply(f'Hey, My bot prefix is {main.prefix}')

        await self.client.process_commands(message)


def setup(client: commands.Bot):
    client.add_cog(OnMessage(client))
