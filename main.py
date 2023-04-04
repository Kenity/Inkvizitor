
import discord
from discord.ext import commands
import os
from config.cfg import setting
import asyncio
import logging

discord.utils.setup_logging()

# or, for example
discord.utils.setup_logging(level=logging.INFO, root=False)
mems = 1
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("!"),
    description='Relatively simple music bot example',
    intents=intents,
	)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load_extensions()
        await bot.start(setting['token'])



asyncio.run(main())