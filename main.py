import discord
import asyncio

from discord.ext import commands
from discord.utils import get
from Game.Player import Player
from Game.Pokestats import Get_Pokemon
from Game.Pokestats import Get_Attacks

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
async def NewPokemon(ctx, inputArg):
    PokeFile = open('Pokemon_txt', 'r')
    print('NewPokemon')
    message = inputArg
    user = ctx.message.author
    if(check_player(ctx, user)):
        ret = players[user].add_pokemon(message, PokeFile)
        if(ret == True):
            print('found running')
            await ctx.send(str(user) + ' Pokemon Has Been Added!')
        elif(ret == False):
            print('not found and running')
            await ctx.send(str(user) + ' Pokemon Not Found!')
    else:
        await ctx.send(str(user) + " You Have to Join First!")

@bot.command()
async def mypokemon(ctx):
    user = ctx.message.author
    pokemon_list = players[user].get_pokemon()
    i = 0
    for name in pokemon_list:
        if(i == 0):
            reply = str(name)
        else:
            reply = (str(reply) + ', ' + str(name))
        i += 1
    await ctx.send(str(user) + ': ' + str(reply))

bot.run(token.read())