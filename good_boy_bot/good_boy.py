# Work with Python 3.6
import discord
import random
import giphy_client
from giphy_client.rest import ApiException

discord_token = INSERT_TOKEN_HERE
giphy_token = INSERT_TOKEN_HERE

client = discord.Client()
api_instance = giphy_client.DefaultApi()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    print(message.content.lower())
    channel = message.channel

    if "good boy" in message.content.lower():
        gif = await search_gifs("happy+dog")
        await channel.send(gif)

    # if message.content.startswith('!hello'):
    #     msg = 'Hello {0.author.mention}'.format(message)
    #     await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

async def search_gifs(query):
    try:
        response = api_instance.gifs_search_get(giphy_token, 
            query, rating='g')
        lst = list(response.data)
        choice = random.randrange(25)

        return lst[choice].url

    except ApiException as e:
        return "Exception when calling DefaultApi->gifs_search_get: %s\n" % e

client.run(discord_token)