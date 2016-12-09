import discord
import asyncio

client = discord.Client()

@client.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
@asyncio.coroutine
def on_message(message):
     rolelist = message.author.roles
     for x in rolelist:
        if str(x) == "###": #Insert Role Name Here
            if x.colour.value == 3066993:
                x.colour = x.colour.red()
                yield from client.edit_role(x.server, x)
                break
            if x.colour.value == 15158332:
                x.colour = x.colour.green()
                yield from client.edit_role(x.server, x)
                break
            if x.colour.value != 15158332 and x.colour.value != 3066993:
                x.colour = x.colour.green()
                yield from client.edit_role(x.server, x)
                break



            
client.run('###') #insert token here
