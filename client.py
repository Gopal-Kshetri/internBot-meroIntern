from pydoc import cli
from urllib import response
from click import command
import discord
import random

TOKEN='OTc3NTk3NDUzODgyNzY5NDc5.G5hDjA.4oDtOJjBIIzdN4ap9zbBcmOcjE8yab4R-Ej8Wc'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, Welcome to the HELL!'
    )


# #------Exception Handling---------------
# @client.event
# async def on_error(event, *args, **kwargs):
#     with open('err.log', 'a') as f:
#         if event == 'on_message':
#             f.write(f'Unhandled message: {args[0]}\n')
#         else:
#             raise



@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the :100: emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool,   '
            'no doubt no doubt no doubt. '
        ),

    ]

    friends_quotes = [
        'Well, maybe I don\'t need your money. Wait, wait, I said maybe!',
        'We were on a break!',
        'Joey doesn\'t share food!',
        'See? He\'s her lobster.',
        'Hi, I\'m Chandler. I make jokes when I\'m uncomfortable.',
        'I wish I could, but I don\'t want to.',
        'Seven!',
        'Pivot!',
        'Could I be wearing any more clothes?',
        'It tastes like feet!',
        (
            'What\'s not to like?',
            'Custard: good.',
            'Jam: good',
            'Meat:GOOD',
        ),
        'This is all a moo point.',
        'Your little Harmonica is hammered.',
        'Can\'t hold her own head up, but yeah - jumped.',
        'And I have to live with a boy!',
        'How you doin\'?',
        'Oh. My. God.',
        'I don\'t even have a \'pla\'',
        'Okay, you have to stop the Q-Tip when there\'s resistance.',
        'Oh, come on, Will, just take off the shirt and tell us.',
        'Nestle Toulouse.',
        'They don\'t know that we know they know we know.',
        'You can\'t just give up. Is that what a dinosaur would do?', 
        'Come on, Ross, you\'re paleontologist. Dig a little deeper.',
        'I got off the plane.',

    ]   

    if message.channel.name == 'bot-test':
        if message.content.lower() == '!gg':
            # response = random.choice(brooklyn_99_quotes)
            response = random.choice(friends_quotes)
            await message.channel.send(response)
            return

        elif message.content.lower() == '!raise-exception':
            raise discord.DiscordException  
        
        if 'happy birthday' in message.content.lower():
            await message.channel.send('Happy Birthday! :balloon::tada: ')
            return

#------- test commands-----------------------
# @client.event
# async def on_message(message):
#     username = str(message.author).split('#')[0]
#     user_message = str(message.content)
#     channel = str(message.channel.name)
#     print(f'{username}: {user_message} ({channel})')


#     if message.author == client.user:
#         return

#     if message.channel.name == 'bot-test':
#         if user_message.lower() == '!hello':
#             await message.channel.send(f'Hello {username}!')
#             return
#         elif user_message.lower() == '!exit':
#             await message.channel.send(f'See you later {username}!')
#             return

#         elif user_message.lower() == '!quote':
#             response = f'You are too sweet. Love you 3000' #{random.randrange(30000)}'
#             await message.channel.send(response)
#             return

#         elif user_message.lower() == '!help':
#             response = f'``` HELP \n !hello: Greets you \n !exit: Goes offline \n !quote : Displays Quote```'
#             await message.channel.send(response)
#             return

    
#     if user_message.lower() == '!anywhere':
#         await message.channel.send('This can be used anywhere')
#         return

#     if (user_message.lower() == '!hello') or (user_message.lower() == '!exit') or (user_message.lower() == '!quote') :
#         await message.channel.send('Only available in `#bot-test` channel')
#         return

client.run(TOKEN)