import discord
 
GUILD = 'R6S'

class MyClient(discord.Client):
	async def on_ready(self):
		guild = discord.utils.get(self.guilds, name=GUILD)
		print(
			f'{self.user} is connected to the following guild:\n'
			f'{guild.name}(id: {guild.id})'
		)
		for guild in self.guilds:
			for member in guild.members:
				print(f'{member}')

	async def on_member_join(self,member):
		await member.create_dm()
		await member.dm_channel.send(f'Welcome {GUILD},{member.name}')

	
	async def on_message(self, message):
		if message.author == self.user:
			return
		elif message.content.startswith('$hello'):
			await message.channel.send('Hello :eyes:')
		elif message.content == "$help":
			await message.channel.send('```Help Commands \n```')
		elif message.content == "$ping":
			guild = message.guild
			await message.author.create_dm()
			await message.author.dm_channel.send(f'Welcome to {GUILD},')
			

client = MyClient(intents=discord.Intents.all())
client.run('ODc1ODAxMzg1NjAwNDMwMTIw.YRazmQ.FQHaLsp4pJ4OikvV_OVZP83UpzI')
