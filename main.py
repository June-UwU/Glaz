#4717
import discord
 
Client = discord.Client()
GUILD = 'R6S'

class MyClient(discord.Client):
	async def on_ready(self):
		guild = discord.utils.get(self.guilds, name=GUILD)
		print(
			f'{self.user} is connected to the following guild:\n'
			f'{guild.name}(id: {guild.id})'
		)

	async def on_member_join(self,member):
		await member.create_dm()
		await member.dm_channel.send(f'Welcome {GUILD},{member.name}')

	
	async def on_message(self,message):
		if message.author == Client.user:
			return
		elif message.content.startswith('$hello'):
			await message.channel.send('Hello :eyes:')
		elif message.content == "$help":
			await message.channel.send('```Help Commands \n```')
		elif message.content == "$ping":
			member = message.author
			await member.create_dm()
			await member.dm_channel.send(f'Welcome {GUILD},{member.name}')
			print(f'{member.id}')


client = MyClient()
client.run()