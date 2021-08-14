import discord
 
GUILD = 'R6S'

class MyClient(discord.Client):
	async def on_ready(self):
		guild = discord.utils.get(self.guilds, name=GUILD)
		print(
			f'{self.user} is connected to the following guild:\n'
			f'{guild.name}(id: {guild.id})'
		)
		await guild.create_role("Big pp guy")

	async def on_member_join(self,member):
		await member.create_dm()
		await member.dm_channel.send(f'Welcome {GUILD},{member.name}')

	
	async def on_message(self, message):
		if message.author == self.user:
			return
		elif message.content == "$hello":
			await message.channel.send('Hello :eyes:')
		elif message.content == "Role":
			if message.author.administrator:
				message.author.add_roles("Big pp guy")
		elif message.content == "$help":
			await message.channel.send('```Help Commands \n```')
		elif message.content == "$ping":
			guild = message.guild
			await message.author.create_dm()
			await message.author.dm_channel.send(f'boop {message.author.name}')
			

client = MyClient(intents=discord.Intents.all())
client.run('ODc1ODAxMzg1NjAwNDMwMTIw.YRazmQ.zBOxd7qWuwceHKspbFmmn03C8dQ')
