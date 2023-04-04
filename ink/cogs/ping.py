import discord
from discord.ext import commands
from discord import app_commands

class PingCommand(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def sync(self, ctx) -> None:
		fmt = await ctx.bot.tree.sync(guild = ctx.guild)
		await ctx.send(
			f"Synced {len(fmt)}"
		)
		return

	@app_commands.command(name = "ping")
	async def ping(self, interaction: discord.Interaction):
		
		await interaction.response.send_message(f"Pong")
	
async def setup(bot):
	await bot.add_cog(PingCommand(bot), guilds = [discord.Object(id = 947084807484104745)])