#Imports
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import datetime
from datetime import timedelta
import random

#Set prefix character
prefix = "."

TargetDate = 0
TargetDate = datetime.datetime.now() + timedelta(seconds=30)
randomSeconds = 0

#Other vars
wordin = ""
listOfWords = ""

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
    responseList = {
        "Ooer",
        "*Hick*",
        "Unreal",
        "Y-y-y'know something. I-I bet crabs think *uuurp* I bet crabs think that fish can fly"

        }
    
    return responseList[random.randint(0,len(reponseList))]

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

        elif(message.content == (prefix + "getChannelID")):
            await client.send_message(client.get_channel(message.channel.id), str(message.channel.id))

        elif(message.content == (prefix + "ping")):
            await client.send_message(client.get_channel(message.channel.id), "Uuurp Pong!")

    elif(TargetDate == datetime.datetime.now()):
        log("Random response date reached")
        #Get random response
        await client.send_message(client.get_channel(getChannel()), getRandomRespose())

        #Get next date
        randomSeconds = random.randint(60,3600)
        TargetDate = TargetDate + timedelta(seconds=randomSeconds)
        log("Target date set as" + str(TargetDate))

    else:
        pass
    

#Run bot
client.run(str(getToken()))
