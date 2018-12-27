import random
import discord
import time
from discord.ext.commands import Bot
import os


BOT_PREFIX = 'c!'
client = Bot(command_prefix=BOT_PREFIX)

############

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="being fabulous"))

############

@client.command(name='hello')

async def hello():
    await client.say("I'm ***CHAD***")


@client.command(name='x28')

async def x28():
    await client.say("***28 STAB WOUNDS***")


@client.command(name='alexa')

async def alexa():
    await client.say("playing Despacito now, yo" + "\n https://www.youtube.com/watch?v=kJQP7kiw5Fk")


@client.command(name='amirite')

async def amirite():
    await client.say("Hell yeah")


@client.command(name='defendme',
                pass_context=True)

async def defendme(context):
    await client.say("Back off, cunt face. Leave " + context.message.author.mention + " alone")


@client.command(name='enoch')

async def enoch():
    await client.say("Enoch is my freaky brother. He thinks he's better than me just cuz he has class but we all know I'm the favorite and so much better than him")
    
 
@client.command(name='haterslurk')

async def haterslurk():
    await client.say("*looks at them* PERISH")
    

@client.command(name='oof')

async def oof():
    await client.say("*OOF*")
    

@client.command(name='philosophy')

async def philosophy():
    possible_responses = [
        "every time you fall asleep, you die. Someone else wakes up in your body thinking they are you. You are alone, trapped in your own mind. The world around you is your lie. Soon, you will be nothing. You will never again hear sounds, never again see colors, never again be anyone.",
        "Death is nothing but an illusion. We glorify it yet also think of it as the worse thing that could ever happen to a person but nobody knows what happens when the lights go out. Are we reincarnated? Do we move on to this so-called Heaven? Hell? I can tell you for a fact that none of those are true. The sweet release of death is anything but what anyone would expect or hope for. It's cruel and messy. An empty void where we drift into nothingness. Absolute nothingness. Nothing special. We drift through the endless abyss of death. No one can ever escape. You're just a ghost floating through time. No thoughts go through your head. What is there to think about? Nothing. Life is meaningless when it's over. No fulfillment. Just emptiness. Trapped in your own mind for eternity. A lost soul with no purpose. No soul has a purpose after death. Nothing."
        ]
    await client.say(random.choice(possible_responses))


@client.command(name='hugme',
                pass_context=True)

async def hugme(context):
    await client.say("hugs " + context.message.author.mention + "! Kyu!")


@client.command(name='hug',
                pass_context=True)

async def hug(context, target: discord.Member):
    await client.say(target.mention + " you have been hugged by " + context.message.author.mention + "! Kyu!")


##################

@client.event
async def on_message(message):
    server = message.server
    message.content = message.content.lower()

    if message.author == client.user:
        return
    elif message.content.startswith("i love you chad"):
        await client.send_message(message.channel, "Who doesn't?!")
    elif "chad" in message.content:
        await client.send_message(message.channel, "I AM *CHAD* \n bow before me, mortals")
    elif "vore" in message.content:
        await client.send_message(message.channel,"***NO VORE***")
        embed = discord.Embed()
        embed.set_image(url="https://media.discordapp.net/attachments/476166668469665821/508337730611314690/Spray.gif")
        await client.send_message(message.channel,embed=embed)
        
    await client.process_commands(message)

    
        
##################

    
client.run(str(os.environ.get("TOKEN")))
