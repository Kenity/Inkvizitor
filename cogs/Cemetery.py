import discord 
from discord.ext import commands, tasks
from discord import app_commands
import asyncio 
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

class Cemeterys(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.cemetry.start()
		
		
	
	
	@tasks.loop(seconds = 0.5)
	async def cemetry(self):
		guild = self.bot.get_guild(947084807484104745)
		print(guild)
		channel = self.bot.get_channel(1082295274090807327)
		
		if channel != None:
			print(channel.members)
			if len(channel.members) > 0:
				try:
					voice_bot = await channel.connect()
					player = discord.utils.get(self.bot.voice_clients)
					player.play(discord.FFmpegPCMAudio('cogs/song.mp3'))
					
				except:
					pass
				
				if len(channel.members) > 1:
					pass
				else:
					member = discord.utils.get(guild.members, id = 1092385818003394631)
					print(member)
					await member.move_to(None)

			

		
		

		

		









async def setup(bot):
	await bot.add_cog(Cemeterys(bot), guilds = [discord.Object(id = 947084807484104745)])