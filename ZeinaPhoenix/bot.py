import discord
from discord.ext import commands
import os
import random

client = commands.Bot(command_prefix = 'z.')

@client.event #Indicates Status
async def on_ready(): #Status
    await client.change_presence(status = discord.Status.online, activity = discord.Game('with data. Hello crew!'))
    print('I am online, Captain.')

path = os.getcwd()
#Go through all the files in cogs and load them.
for filename in os.listdir(path + '\ZeinaPhoenix\cogs'): #Load Cogs
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


#Events

@client.event #If a memeber enters
async def on_member_join(member):
    print(f'(member) has joined the server.')

@client.event #If a memeber exits
async def on_member_remove(member):
    print(f'(member) has left the server.')

@client.event #Message responses
async def on_message(message):
    if message.author == client.user:
        return

    #Response to Hello
    if message.content.startswith('Zeina, hello'):
        hello_to_me = random.choice(['Hello!',
                                    'Hey!',
                                    'Hola!',
                                    'Bonjour!',
                                    'Ciao!',
                                    'Здравствуйте!',
                                    'Hallo!',
                                    'Merhaba!',
                                    'こんにちは!'])
        await message.channel.send(hello_to_me)
    #Response to How Are You?
    elif message.content.startswith('Zeina, how are you'):
        how_am_i = random.choice(['I am fine, thank you!',
                                'Great! Thanks for asking!',
                                'My systems are running as expected.',
                                'Up and running normally.'])
        await message.channel.send(how_am_i)
    #Response to What Are You Doing?
    elif message.content.startswith('Zeina, what are you doing'):
        what_i_do = random.choice(['Doing my tasks',
                                'Supervising the crew.',
                                'Analyzing my programming.',
                                'Checking if Alexander added a new module.',
                                'Taking care of the data.'])
        await message.channel.send(what_i_do)
   
    await client.process_commands(message)    

@client.event #Error responses
async def on_command_error(ctx, error): #Error Respond
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all required arguments.')
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid Command. Write z.help if you have doubts.')


#Primary Tools

@client.command() #Load cog
@commands.has_permissions()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send('Module loaded')

@client.command() #Unload cog
@commands.has_permissions()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send('Module unloaded')

@client.command() #Reload cog
@commands.has_permissions()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send('Module reloaded')

@client.command() #Clearing messages
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount = 5):
        await ctx.channel.purge(limit=amount)


#Secondary Tools

@client.command() #Ping
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)} ms")

client.run('NzU4MTYyNjc0NDc0NTQ5MjY4.X2q8Aw.qGrUe28Xy5k8LWr9fZAawVjq_KI')
