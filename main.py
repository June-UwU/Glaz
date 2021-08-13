import discord
 
Client = discord.Client()

@Client.event
async def on_ready():
	print(f'{Client.user} has connected to Discord!')

Client.run("ODc1ODAxMzg1NjAwNDMwMTIw.YRazmQ.EaRcqOZV-92xUgQnMKBp94zDV88")