import os

import discord
from discord.ext import commands

from bot.database.manager import main as db_main

client = commands.Bot(command_prefix=db_main.prefix)

for filename in os.listdir('./bot/cogs'):
    if filename.endswith('.py'):  # cogs.musicplayer is not being loded in here
        try:
            client.load_extension(f'bot.cogs.{filename[:-3]}')
            print(f"[+] Loaded: bot.cogs.{filename[:-3]}")
        except Exception as excl:
            print(
                f"[+] Unable to load: bot.cogs.{filename[:-3]}  :  {excl}")


# client.run(db_main.token)
