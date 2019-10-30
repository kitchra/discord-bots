# Work with Python 3.6
import discord

TOKEN = INSERT_TOKEN_HERE

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    await_client.send_message(client.emojis[0])

    for emoji in client.emojis:
        if emoji.name in message.content:
            await_client.send_message(message.channel, str(emoji))
            print("Emoji found")
            print(emoji.name)

    # if message.content.startswith('!hello'):
    #     msg = 'Hello {0.author.mention}'.format(message)
    #     await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)