# bot.py
import os
import random

import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import CommandNotFound

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
bot = commands.Bot(command_prefix='!')

#Dictionary where key is the name and value is message.
secrets = {}

truthIndex = 0
dareIndex = 0

@client.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hey {member.name}, bend over and show me your feet.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    replies = [f'Fuck you {message.author}, I don\'t care', 'That\'s cool... oh wait it\'s not', 'Great -_-', f'Wow {message.author}, you\'re so cool and quirky', 'Go away gimp', f'Suck yourself {message.author}']

    if 'peppa' in message.content.lower():
        response = random.choice(replies)
        await message.channel.send(response)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='rolldice', help='Simulates rolling dice.')
async def roll(ctx):
    dice = str(random.choice(range(1, 7)))
    await ctx.send(dice)

@bot.command(name='flipcoin', help='Simulates flipping a coin.')
async def flip(ctx):
    outcomes = ['Heads!', 'Tails!']
    coin = str(random.choice(outcomes))
    await ctx.send(coin)

@bot.command(name='tellon', help='Private message Peppa saying !tellon name "message" to tell it a secret about someone (make sure to keep message in speech marks).')
async def tell(ctx, person, message):
    global secrets
    await ctx.author.send(f'Thanks for telling me about {person} :)')
    label = person.lower()
    if label not in secrets:
        temp = []
        secrets[label] = temp
    secrets[label].append(message.lower())
    print(secrets)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        print('Some retard used a command that doesn\'t exist.')
        return
    raise error

@bot.command(name='callout', help='In the general chat use !callout name to bait someone out.')
async def callout(ctx, person):
    global secrets
    #channel = discord.utils.get(client.get_all_channels(), guild__name='Jynxer\'s Emporium', name='general')
    if person.lower() in secrets:
        secret = random.choice(secrets[person.lower()])
        await ctx.send(f'I\'ve heard that {secret}')
    else:
        await ctx.send(f'I don\'t know anything about {person} :(')

@bot.command(name='roast', help='Roasts somebody.')
async def roast(ctx, person):
    roasts = [f'I hate you {person}, you\'re a cunt', f'Hey {person}, your mum is so fat that she is gay', f'Shut the fuck up {person} you dirty faggot, I\'m going to rape your whole family and give you cancer', f'I would rather push nails into my eyeballs than spend time with {person}.', f'{person} is a silly ginger cunt with no pubes.', f'I would rather get gangrene in my testicles than speak to {person} for one more second.', f'{person}\'s mum wears her flaps as a facemask.', f'Hi my name is {person} and im a sex offender LOOOOL {person} is a loser.', f'{person} ur mum and ur sister both have discharge sweets that they sell to foetuses for a small price then they gw']
    message = str(random.choice(roasts))
    await ctx.send(message)

def resetTruths():
    global truthIndex
    truthIndex = 0

def resetDares():
    global dareIndex
    dareIndex = 0

@bot.command(name='truth', help='Get a truth.')
async def truth(ctx):
    global truthIndex
    #truths = ["Testing 1", 'Testing 2', 'Testing 3']
    truths = ['What are your top three turn-ons?', 'What is your deepest darkest fear?', 'Tell me about your first kiss.', 'Who is the most attractive person from your secondary school?', 'Who is the least likely to clutch a 1v2', 'What is your biggest regret?', 'Who have you had a crush on that you never told anyone about?', 'Who was the last person you licked?', 'Have you ever cheated or been cheated on?', 'Tell me about your most awkward date.', 'What are you most self-conscious about?', 'When was the last time you peed in bed?', 'What is the biggest lie you have ever told?', 'Who is the person you most regret kissing?', 'What is the naughtiest thing you\'ve done in public?', 'What do most people think is true about you, but isn\'t?', 'What is the biggest thnig you\'ve gotten away with?', 'What would you do if you were the opposite sex for a month?', 'What is the most childish thing you still do?', 'What is your secret sexual fantasy?', 'If you could have sex with anyone who would it be?', 'Where is the strangest place you have peed?', 'What is the most embarrasing thing your parents have caught you doing?', 'What is the most embarrasing thing in your room?', 'What is the stupidest thing you have ever done?', 'What was the most awkward romantic encounter you have had?', 'What is the weirdest thing you\'ve done with someone of the opposite gender?', 'What do you really hope your parents never find out about?', 'What have you done that people here would judge you most for doing?']
    if (truthIndex >= len(truths)):
        resetTruths()
    message = str(truths[truthIndex])
    truthIndex = truthIndex + 1
    await ctx.send(message)

@bot.command(name='dare', help='Get a dare.')
async def dare(ctx):
    global dareIndex
    dares = ['Eat two tablespoons of a condiment.', 'Eat one tablespoon of instant coffee.', 'Let the group give you a new hairstyle.', 'Do your best impression of a baby being born.', 'Put 4 ice-cubes down your pants.', 'Lick the ground.', 'Dance with no music for one minute.', 'Play a song by slapping your bum until someone guesses the song.', 'Let one of the group message someone on your phone.', 'Write something of the group\'s choosing somewhere on your body.', 'Let someone choose something for you to draw on your face.', 'Gargle something that shouldn\'t be gargled.', 'Spin an imaginary hula hoop around your waist for one minute.', 'Sing a song about someone of your own choosing.', 'Take off your underwear and wear it on your head for 5 minutes.', 'Eat one teaspoon of the spiciest thing you have in the kitchen.', 'Call the 7th contact in your phone and sing them 30 seconds of a song that the group chooses.', 'Drop something in the toilet and then reach in to get it.']
    if (dareIndex >= len(dares)):
        resetDares()
    message = str(dares[dareIndex])
    dareIndex = dareIndex + 1
    await ctx.send(message)

bot.run(TOKEN)
#client.run(TOKEN)
