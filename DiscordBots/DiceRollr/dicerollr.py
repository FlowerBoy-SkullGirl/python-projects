import discord
import random

help_command = 'To make a roll do "!roll {d}#" where # is the sides of the dice and the d is optional\nTo do a more advanced roll do !roll (# of dice) ({d}#) ({+,-}#) ({a,d}) where a or d are advantage or disadvantage and are optional. You must use every preceding option to use the next. For example, for a d20 + 5, you should do !roll 1 d20 +5'

def roll_dice(dn,ds,da,d_sign,nr):
    totals = []
    for i in range(nr):
        total = 0
        for j in range(dn):
            total += (random.randint(1,ds))
        total += (da * d_sign)
        totals.append(total)
    if len(totals) == 1:
        return_string = "You rolled {}!".format(totals[0])
        return return_string
    if len(totals) == 2:
        return_string = "You rolled {} and {}!".format(totals[0],totals[1])
        return return_string

def parseCommand(command):
    #vars to send to roll func
    diceNum = 1
    diceSides = 1
    diceAdd = 0
    diceSign = 1
    numRolls = 1

    if command.startswith('!roll help') or command == '!roll':
        return help_command
    commands = command.split(' ')

    if len(commands) == 2:
        if 'd' in commands[1]:
            commands[1] = commands[1].strip('d')
        try:
            diceSides = int(commands[1])
        except:
            return help_command
        return roll_dice(diceNum,diceSides,diceAdd,diceSign,numRolls)
        
    if len(commands) == 3:
        try:
            diceNum = int(commands[1])
        except:
            return help_command
        if 'd' in commands[2]:
            commands[2] = commands[2].strip('d')
        try:
            diceSides = int(commands[2])
        except:
            return help_command
        return roll_dice(diceNum,diceSides,diceAdd,diceSign,numRolls)
    
    if len(commands) == 4:
       try:
           diceNum = int(commands[1])
       except:
           return help_command
       if 'd' in commands[2]:
           commands[2] = commands[2].strip('d')
       try:
           diceSides = int(commands[2])
       except:
           return help_command
       if commands[3].startswith('-'):
           commands[3] = commands[3].strip('-')
           diceSign = -1
       if commands[3].startswith('+'):
           commands[3] = commands[3].strip('+')
       try:
           diceAdd = int(commands[3])
       except:
           return help_command

       return roll_dice(diceNum,diceSides,diceAdd,diceSign,numRolls)


    if len(commands) > 4:
       try:
           diceNum = int(commands[1])
       except:
           return help_command
       if 'd' in commands[2]:
           commands[2] = commands[2].strip('d')
       try:
           diceSides = int(commands[2])
       except:
           return help_command
       if commands[3].startswith('-'):
           commands[3] = commands[3].strip('-')
           diceSign = -1
       if commands[3].startswith('+'):
           commands[3] = commands[3].strip('+')
       try:
           diceAdd = int(commands[3])
       except:
           return help_command
       numRolls = 2
       return roll_dice(diceNum,diceSides,diceAdd,diceSign,numRolls)
    return help_command


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == client.user:
            return
        if message.content.startswith('!roll'):
            print(f'Roll received {message.content}')
            parsed = parseCommand(message.content)
            await message.reply(parsed, mention_author=True)

intents = discord.Intents.default()
intents.message_content = True

random.seed()

fileToken = open("token", "r")
token = fileToken.readline()

client = MyClient(intents=intents)
client.run(token)
