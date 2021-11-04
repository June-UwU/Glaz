import discord
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = ''
GUILD = 'R6S'

class MyClient(discord.Client):
	async def on_ready(self):
		guild = discord.utils.get(self.guilds, name=GUILD)
		print(
			f'{self.user} is connected to the following guild:\n'
			f'{guild.name}(id: {guild.id})'
		)
		#print(len("$Getrole"))

	async def on_member_join(self,member):
		await member.create_dm()
		await member.dm_channel.send(f'Welcome {GUILD},{member.name}')
		member.guild_permissions.update()

	async def on_reaction_add(self,reaction, user):
		channel = reaction.message.channel
		await channel.send(f'{user} gave reaction to {reaction.message.author.name}')



	async def on_message(self, message):
		if message.author == self.user:
			return
		elif message.content.startswith('$ping'):
			guild = message.guild
			await message.author.create_dm()
			await message.author.dm_channel.send(f'boop {message.author.name}')
		elif message.content.startswith('$Scalpel'):
			await message.channel.send("lub you doc..")
		elif  message.content.startswith('$help'):
			await message.channel.send('```Help Commands \n```')
		elif message.content.startswith('$hello'):
			await message.channel.send('Hello :eyes:')
		elif message.content.startswith('$Createrole'):
			if message.author.guild_permissions.manage_roles | message.author.guild_permissions.administrator:
				Rolename = ''
				Permission  = discord.Permissions(add_reactions = True, attach_files = True,change_nickname = True
						,connect = True,create_instant_invite = True,embed_links = True,external_emojis = True,read_messages = True
						,read_message_history = True,send_messages = True,speak  = True,stream = True,view_channel = True) 
				Guild = message.guild
				for z in range(len('$Createrole')+1,len(message.content)):
					if message.content[z] == '-':
						symbol = message.content[z] + message.content[z+1]
						if symbol == '-N':
							count = z + 2
							for k in range(count , len(message.content)):
								if message.content[k] == ',':
									z = count
									break
								elif message.content[k] == '"':
									continue
								else:
									Rolename = Rolename + message.content[k]
						elif symbol == '-A':
							Permission = discord.Permissions.all()
							z += 2
						elif symbol == '-a':
							Permission = discord.Permissions.advanced()
							z+= 2
						elif symbol == '-C':
							Permission = discord.Permissions.all_channel()
							z+= 2
						elif symbol == '-G':
							Permission = discord.Permissions.general()
							z+= 2
						elif symbol == '-M':
							Permission = discord.Permissions.membership()
							z+= 2
						elif symbol == '-N':
							Permission = discord.Permissions.none()
							z+= 2
						elif symbol == '-s':
							Permission = discord.Permissions.stage()
							z+= 2
						elif symbol == '-S':
							Permission = discord.Permissions.stage_moderator()
							z+= 2
						elif symbol == '-T':
							Permission = discord.Permissions.text()
							z+= 2
						elif symbol == '-V':
							Permission = discord.Permissions.voice()
							z+= 2
						else:
							await message.channel.send("invalid command")
						await Guild.create_role(name = Rolename,permissions = Permission)
			else:								
				await message.channel.send("Nice try :), but I thought ahead -June")
		elif message.content.startswith('$getrole'):
			name = ''
			for i in range(len('$Getrole')+1,len(message.content)):
				name += message.content[i]

			member = message.guild.get_member_named(name)
			text = ''
			for i in range(1,len(member.roles)):
				text = member.roles[i].name + ''
			await message.channel.send(f'{text}')
		elif message.content.startswith('$ban'):
			if message.author.guild_permissions.kick_members:
				name = ''
				cause = ''
				print(len('$ban'))
				z = len('$ban')+1
				if message.content[z] == '-':
					symbol = message.content[z] + message.content[z+1]
					count = z+2
					if symbol == '-U':
						for k in range(count + 1, len(message.content)):
							if message.content[k] == ',':
								z = k + 1
								break
							elif message.content[k] == '"':
								continue
							else:
								name = name + message.content[k]
					elif symbol == '-R':
						for k in range(count, len(message.content)):
							if message.content[k] == ',':
								z = k + 1
								break
							elif message.content[k] == '"':
								continue
							else:
								cause += message.content[k]
					if(cause == ''):
						cause = "N/A"
					for memb in message.guild.members:
						if memb.name == name:
							await message.channel.send(f"Banned {name}")
							await message.channel.send(f'Banned for : {cause}')
							await message.guild.ban(user = memb,reason = cause)
							break
						else:
							continue
#Userroles - 9

client = MyClient(intents=discord.Intents.all())
client.run(TOKEN)