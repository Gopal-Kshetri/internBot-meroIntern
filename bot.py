from discord.ext import commands
import discord

from merointern import intern_meroIntern
from friends import friends_quote
from roast import roast_me

TOKEN='OTc3NTk3NDUzODgyNzY5NDc5.G5hDjA.4oDtOJjBIIzdN4ap9zbBcmOcjE8yab4R-Ej8Wc'

bot = commands.Bot(command_prefix='!', help_command=None)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected!')

@bot.command(name='help', help='Commands for the Discord bot')
async def help(ctx):
    embed=discord.Embed(
        title="Help", 
        description="Commands for botSoy", 
        color=discord.Color.orange()
        )
    embed.set_author(
        name=ctx.author.display_name, 
        url="https://twitter.com/RealDrewData", 
        icon_url=ctx.author.avatar_url
        )
    embed.set_thumbnail(url="https://merointernship.com/wp-content/uploads/2021/09/coverimages-01-630x230.jpg")

    bot_commands = ['help', 'quote', 'roast', 'interns']
    descriptions = ['Displays commands for the Discord bot', 'Responds with a random quote from Friends', 'Roasts you with Yo mama joke', 'Provides you the available interns']
    for (bot_command,description) in zip(bot_commands, descriptions):
        embed.add_field(name=f'**{bot_command}**', value=f'> {description}', inline=False)

    await ctx.send(embed=embed)
#     await ctx.send(
# """```Help    Commands for the Discord bot
# gg      Responds with a random quote from Friends
# roast   Roasts you with Yo mama joke
# interns  Provides you the available interns```"""
#     )


@bot.command(name = 'interns', help='Embed in Discord')
async def interns(ctx):
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


@bot.command(name='quote', help='Responds with a random quote from Brooklyn 99')
async def quote(ctx):
    
    brooklyn_99_quotes = [
        'I\'m the human form of the :100: emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool,   '
            'no doubt no doubt no doubt. '
        ),
    ]

    response = friends_quote()
    await ctx.send(response)


@bot.command(name='roast', help='Roasts you with mom joke')
async def roast(ctx):
    response = roast_me()
    await ctx.send(response)


bot.run(TOKEN)