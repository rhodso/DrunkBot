#Imports
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import datetime
from datetime import timedelta
import random
import praw

#Reddit variables
CLID = "IGAjcEE-70TWfw"
SECT = "zu64wRhKJHCoGHX0HDLh2L34Idk"
AGNT = "ChatBot"
reddit = praw.Reddit(client_id=CLID, client_secret=SECT, user_agent=AGNT)

#Set prefix character
prefix = "."

#Def log method
def log(Message):
    print(str(datetime.datetime.now())+ '   ' + str(Message))

#Def Method to read token from the file
def getToken():
    tokenFile = open('token.txt','r')
    token = tokenFile.read()
    return token

#Define client
client = Bot(description='', command_prefix=prefix, pm_help = False)

#Startup sequence
@client.event
async def on_ready():
    log('Initialising...')
    log('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    log('')
    log('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
    log('Ready!')
    return await client.change_presence(game=discord.Game(name='a drinking game')) 

#Get random reponse
def getRandomRespose():
    responseList = [
        "Ooer",
        "*Hick*",
        "Unreal",
        "Y-y-y'know something. I-I bet crabs think *uuurp* I bet crabs think that fish can fly",
        "You sure do got a- *hick* a-a-a purdy mouf",
        "Look at mah truck nuts!",
        "I don't fuck mah seester, I make love to 'er",
        "No, Officer... I *uurp* I-I swear to drunk I'm not god",
        "That ain't beer, that's piss!",
        "PARTY FOUL!",
        "I ytprd it with my nose and 6th to get a free lift to the station at least a bit of the moon through a telescope using it you finish at I don't understand and then replace them when I have the money from work and uni so won't be home until like it's",
        "@ZombieBroth made me, officer",
        "I threw up on my socks.... happy *hick* new year",
        "zzzzzzzzzzzzzzzzzzzzzoooooooooooooooooombie why unot oline hw==whe i neeed oyu",
        "I would call heavan and tell them they're missing an ange- *hick* -angel. But I'm kinda hoping you're a slut",
        "Did you sit in some sugar? Cause you have a *uurp* a sweet looking ass",
        "Girl you should sell hot dogs! You already know how to make a weiner *uurp stand",
        "You remind me of my big toe. I'm going to bang you on every piece of furniture in my house",
        "How about you come over here and sit on my lap. We'll talk about the first thing that pops up",
        "Did you just fart? Because you blew me away"
        ]
    
    return random.choice(responseList)

#Commands
@client.event
async def on_message(message):
    if(message.content[:1] == prefix):
        #If message starts with the prefix, it's a command. Handle it as such

        #Command structure:
        #if(message.content == (prefix + "[Command Invoker]")):
        #   log("Running [Command name] command...")
        #   Do stuff
        #   End with:
        #   await client.send_message(client.get_channel(message.channel.id), [Message (result of command)])
        
        if(message.content == (prefix + "help")):
            log("Running help command...")
            await client.send_message(client.get_channel(message.channel.id), "Uuurp")

        elif(message.content == (prefix + "ping")):
            await client.send_message(client.get_channel(message.channel.id), "Uuurp Pong!")

        elif(message.content == (prefix + "shouldIDrink?")):
            await client.send_message(client.get_channel(message.channel.id), "Yes")

        elif(message.content == (prefix + "iHaveAnIdea")):
            log("Running iHaveAnIdea command")
            submission = reddit.subreddit('crazyideas').random()
            await client.send_message(client.get_channel(message.channel.id), "Yo guys, I got an idea!")
            await client.send_message(client.get_channel(message.channel.id), submission.title)
            await client.send_message(client.get_channel(message.channel.id), submission.selftext)

    elif(random.randint(1,10) == 5):
        if(message.author != "DrunkBot"):    
            log("Message will be replied to")
            await client.send_message(client.get_channel(message.channel.id), getRandomRespose() + ", " + message.author.mention)
    else:
        pass

#Run bot
#client.loop.create_task(background_loop())
client.run(str(getToken()))