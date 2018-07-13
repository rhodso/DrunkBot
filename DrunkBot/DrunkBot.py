#Imports
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import datetime
from datetime import timedelta
import random
from time import gmtime, strftime


#Set prefix character
prefix = "."


#Def log method
def log(Message):
    print(str(datetime.datetime.now())+ '   ' + str(Message))

TargetDate = datetime.datetime.now()
TargetDate = TargetDate + timedelta(seconds=20)
log("Target Date set as: " + str(TargetDate))
randomSeconds = 0

def getTargetDate():
    return TargetDate

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

#Get random channel
def getRandomChannel():
        textChannelList = []
        for server in Client.servers:
            for channel in server.channels:
                if channel.type == 'Text':
                    textChannelList.append(channel.id)

        #return textChannelList[random.randint(0,len(textChannelList))]
        return 334694739020611586 #admin channel on my private server

#Get random reponse
def getRandomRespose():
    responseList = [
        "Ooer",
        "*Hick*",
        "Unreal",
        "Y-y-y'know something. I-I bet crabs think *uuurp* I bet crabs think that fish can fly"

        ]
    
    return random.choice(responseList)

def willBotReply(target, current):
    if(target < current):
        return True
    else:
        return False

#Random response
#async def on_socket_raw_send():

#Commands
@client.event
async def on_message(message):
    TargetDate = getTargetDate()
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

    elif(random.randint(1,10) == 5):
        if(message.author != "ChatBot"):    
            log("Message will be replied to")
            await client.send_message(client.get_channel(message.channel.id), getRandomRespose())
    else:
        pass

#Run bot
client.run(str(getToken()))