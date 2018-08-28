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
    #Create array
    responseList = []
    
    #Read them all into an array
    file = open('responselist.txt', 'r')
    for line in file:
        reponselist.append(line)
    
    #Return one at random
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