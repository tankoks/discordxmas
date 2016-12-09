import discord
import asyncio
import time
import random

client = discord.Client()
@client.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!###'): #insert command text here
        rolelist = message.author.roles
        for x in rolelist:
            if str(x) == "###": #Insert Role Name Here
                while True:
                    x.colour = x.colour.red()
                    await client.edit_role(x.server, x)
                    await asyncio.sleep(random.randrange(5,11))
                    x.colour = x.colour.green()
                    await client.edit_role(x.server, x)
                    await asyncio.sleep(random.randrange(5,11))
                    #x.colour = x.colour.blue()
                    #await client.edit_role(x.server, x)
                    #await asyncio.sleep(1)
                    



client.run('###') #insert token here
