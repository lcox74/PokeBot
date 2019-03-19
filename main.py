import discord
import asyncio
from discord.ext import commands

from Game.Player import Player

prefix = '#'
token = open("TOKEN", "r")
players = {}

bot = commands.Bot(command_prefix=prefix, description='A wild Pokebot has appeared, lets play some pokemon!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

def setup_player(user, force=False):
    players[user] = Player(user, force)

def check_player(ctx, user):
    if(user in players):
        return True
    else:
        return False

@bot.command()
async def join(ctx):
    user = ctx.message.author
    if(user not in players):
        setup_player(user)
        await ctx.send("Done")
    else:
        await ctx.send(str(user) + " Fight or Die, Can't Restart Now!")
    
@bot.command()
async def hurt(ctx):
    user = ctx.message.author
    if(user in players):
        await ctx.send(str(players[user].get_health()))
        players[user].get_hurt()
        await ctx.send(str(players[user].get_health()))
    else:
        await ctx.send(str(user) + ' Gotta join the pokeverse first mate!')

@bot.command()
async def NewPokemon(ctx, *, inputArg = '1'):
    message = await discord.utils.get_text(ctx, inputArg)
    user = ctx.message.author
    if(check_player(ctx, user)):
        reply = players[user].Add_Pokemon(message)
        await ctx.send(str(user) + str(reply))
    else:
        await ctx.send(str(user) + " You Have to Join First!")

bot.run(token.read())