import os
import random
from discord.ext import commands
import discord

from main import intern_meroIntern

TOKEN='OTc3NTk3NDUzODgyNzY5NDc5.G5hDjA.4oDtOJjBIIzdN4ap9zbBcmOcjE8yab4R-Ej8Wc'

bot = commands.Bot(command_prefix='!', help_command=None)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected!')

@bot.command(name='help', help='Commands for the Discord bot')
async def help(ctx):
    await ctx.send(
"""```Help    Commands for the Discord bot
gg      Responds with a random quote from Friends
roast   Roasts you with mom joke
interns  Provides you the available interns```"""
    )

# @bot.command(name='interns', help='Provides you the available interns')
# async def interns(ctx):
#     titles, authors, dates = intern_meroIntern()
#     response = PrettyTable(['Title', 'Author', 'Date'])
#     for (title, author, date) in zip(titles, authors, dates):
#         # print(title+ '\t' + author + '\t' + date + '\t')
#         response.add_row([title, author, date])
#     await ctx.send(response)


@bot.command(name = 'interns', help='Embed in Discord')
async def embed(ctx):
    embed=discord.Embed(
        title="Mero Internship", 
        url="https://merointernship.com/category/internship/", 
        description="Internships Available", 
        color=discord.Color.blue()
        )
    embed.set_author(
        name=ctx.author.display_name, 
        url="https://twitter.com/RealDrewData", 
        icon_url=ctx.author.avatar_url
        )
    embed.set_thumbnail(url="https://merointernship.com/wp-content/uploads/2021/09/coverimages-01-630x230.jpg")
        
    titles, authors, dates = intern_meroIntern()
    for (title, author, date) in zip(titles, authors, dates):
        # print(title+ '\t' + author + '\t' + date + '\t')
        embed.add_field(name=f'**{title}**', value=f'> Author: {author} \n> Date: {date}', inline=False)

    await ctx.send(embed=embed)


@bot.command(name='gg', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    
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

    response = random.choice(friends_quotes)
    await ctx.send(response)


@bot.command(name='roast', help='Roasts you with mom joke')
async def roast(ctx):
    mom_jokes = [
        'Mothers of teens understand why some animals eat their young.',
        '"Mom, what\'s it like to have the greatest daughter in the world?" \n "I don\'t know, ask your grandma!"',
        'Kid: Mom, stop. You aren\'t funny. \n Mom: I made you.',
        'Why did the baby strawberry cry? \n Because his mom was in a jam!',
        'What do you call a small mom? \n Minimum.',
        'Yo Mama\'s like a library, open to the public.',
        'Yo Mama\'s like mustard, she spreads easy.',
        'If Yo Mama and Yo Daddy got a divorce, they\'d still be brother and sister.',
        'Yo Mama\'s so fat her butt cheeks have different area codes.'
    ]

    response = random.choice(mom_jokes)
    await ctx.send(response)



bot.run(TOKEN)