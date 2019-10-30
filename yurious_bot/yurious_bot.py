# Work with Python 3.6
import discord
import random
import giphy_client
from giphy_client.rest import ApiException

discord_token = INSERT_TOKEN_HERE
giphy_token = INSERT_TOKEN_HERE

client = discord.Client()
api_instance = giphy_client.DefaultApi()

#Keep track of the yurious bois in this chat
yurious_bois = dict()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    print(message.content.lower())
    channel = message.channel

    if "yury" in message.content.lower():
        #Don't talk about yury.  There is only yurious.
        gif = await search_gifs("yuri")
        await channel.send(gif)
    elif "yurious" in message.content.lower():
        msg = ""

        if "YURIOUS" in message.content:
            msg += """``` __   ___   _ ___ ___ ___  _   _ ___ 
 \ \ / / | | | _ \_ _/ _ \| | | / __|
  \ V /| |_| |   /| | (_) | |_| \__ \\
   |_|  \___/|_|_\___\___/ \___/|___/
   """
        elif "yUrIoUs" in message.content:
            msg += """```       _   _    ___     _   _    
  _  _| | | |_ |_ _|___| | | |___
 | || | |_| | '_| |/ _ \ |_| (_-<
  \_, |\___/|_||___\___/\___//__/
  |__/                           
  """
        else:
            msg += """```                 _             
  _  _ _  _ _ _(_)___ _  _ ___
 | || | || | '_| / _ \ || (_-<
  \_, |\_,_|_| |_\___/\_,_/__/
  |__/                        
  """

        msg += """               _           
  __ ___ _  _ _ _| |_ ___ _ _ 
 / _/ _ \ || | ' \  _/ -_) '_|
 \__\___/\_,_|_||_\__\___|_|  
                              
"""


        if message.author not in yurious_bois:
            #New yurious boi has appeared
            yurious_bois[message.author] = 1
        else:
            #Increment yurious counter
            yurious_bois[message.author] = yurious_bois[message.author] + 1

        max_fury = 0
        yurious = "Nobody"
        tie = False

        for boi,count in yurious_bois.items():
            if count > max_fury:
                yurious = boi
                max_fury = count
            elif count == max_fury:
                tie = True

            msg += "{name:<20}: {num:<5}\n".format(name=str(boi).split('#')[0], num=int(count))
        
        msg += "```"

        await channel.send(msg)

        if max_fury==0:
            await channel.send("Nobody's yurious? Lame :(")
        elif tie:
            await channel.send("UH OH! There's a tie!")
        else:
            await channel.send("Congrats to {} for being MOST YURIOUS!!!".format(yurious.mention))


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