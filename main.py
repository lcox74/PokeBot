import discord
import asyncio

from discord.ext import commands
from discord.utils import get
from Game.Player import Player
from Game.Pokestats import Get_Pokemon
from Game.Pokestats import Get_Attacks

prefix = 'poke'
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
async def new(ctx, inputArg):
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
async def mine(ctx):
    user = ctx.message.author
    pokemon_list = players[user].get_pokemon()
    user = ctx.message.author
    final_reply = (user.mention + '\n')
    for poke in pokemon_list:
        reply = (str(poke.get_name()) + ' (' + str(poke.get_level()) + '),' +' Health: ' + str(poke.get_health()[0]) +'/'+ str(poke.get_health()[1]) + ','+ ' Attack: ' + str(poke.get_attack()) + ',' +' XP: ' + str(poke.get_xp())+'/'+str(poke.get_level_up()) +','+ ' Types: ' + str(poke.show_type()) + '\n')
        final_reply = final_reply + reply
    await ctx.send(reply)

@bot.command()
async def all(ctx):
    await ctx.send(("Sorry buddy gotta go directly to the source for that:  " + 'https://pokemondb.net/pokedex/all'))

bot.run(token.read())