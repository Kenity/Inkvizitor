import discord 
from discord.ext import commands
import os 
from discord import app_commands



class nakaz(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def nakaz(self, ctx, *,  member: discord.Member):
		channel = ctx.message.author.voice.channel
		print(channel)
		for m in channel.members:
			await m.edit(mute = True)
	@commands.command()
	async def unnakaz(self, ctx, *,  member: discord.Member):
		channel = ctx.message.author.voice.channel
		print(channel)
		for m in channel.members:
			await m.edit(mute = False)

	@commands.command()
	async def voice_nakaz(self, ctx, * , member: discord.Member):
		voice_channel = self.bot.get_channel(1082295274090807327)
		try:
			voice = await voice_channel.connect()
		except:
			pass
		
		song_there = os.path.isfile('song.mp3')
		player = discord.utils.get(self.bot.voice_clients)

		player.play(discord.FFmpegPCMAudio('cogs/song.mp3'))
		voice.source = discord.PCMVolumeTransformer(voice.source)
		voice.source.volume = 0.5









async def setup(bot):
	await bot.add_cog(nakaz(bot), guilds = [discord.Object(id = 947084807484104745)])