import discord
import asyncio

from Game.Player import Player

client = discord.Client()

token = open("TOKEN", "r")

players = {}

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):

    def setupPlayer (force=False):
        players[message.author] = Player(message.author, force)

    if message.content.startswith('!left'):
        if not message.author in players:
            setupPlayer()
        players[message.author].MoveLeft()
        await client.send_message(message.channel, '{} moved left and is now at {}!'.format(message.author, str(players[message.author].GetPosition())))

    elif message.content.startswith('!right'):
        if not message.author in players:
            setupPlayer()
        players[message.author].MoveRight()
        await client.send_message(message.channel, '{} moved right and is now at {}!'.format(message.author, str(players[message.author].GetPosition())))

    elif message.content.startswith('!up'):
        if not message.author in players:
            setupPlayer()
        players[message.author].MoveUp()
        await client.send_message(message.channel, '{} moved up and is now at {}!'.format(message.author, str(players[message.author].GetPosition())))

    elif message.content.startswith('!down'):
        if not message.author in players:
            setupPlayer()
        players[message.author].MoveDown()
        await client.send_message(message.channel, '{} moved down and is now at {}!'.format(message.author, str(players[message.author].GetPosition())))

    elif message.content.startswith('!reset'):
        if message.author in players:
            setupPlayer(True)
        await client.send_message(message.channel, '{} is squeaky clean!'.format(message.author))

client.run(token.read())