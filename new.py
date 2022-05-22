from pydoc import cli
from urllib import response
import discord
import random

TOKEN='OTc3NTk3NDUzODgyNzY5NDc5.G5hDjA.4oDtOJjBIIzdN4ap9zbBcmOcjE8yab4R-Ej8Wc'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')


    if message.author == client.user:
        return

    if message.channel.name == 'bot-test':
        if user_message.lower() == '~hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == '~exit':
            await message.channel.send(f'See you later {username}!')
            return

        elif user_message.lower() == '~quote':
            response = f'You are too sweet. Love you 3000' #{random.randrange(30000)}'
            await message.channel.send(response)
            return

        elif user_message.lower() == '~help':
            response = f'``` HELP \n ~hello: Greets you \n ~exit: Goes offline \n ~quote : Displays Quote```'
            await message.channel.send(response)
            return

    
    if user_message.lower() == '~anywhere':
        await message.channel.send('This can be used anywhere')
        return

    if (user_message.lower() == '~hello') or (user_message.lower() == '~exit') or (user_message.lower() == '~quote') :
        await message.channel.send('Only available in `#bot-test` channel')
        return

client.run(TOKEN)