# modules
import random
import discord
import asyncio
import datetime
import time

from datetime import datetime
from random import randint
from discord.ext import commands
from discord.ext.commands import *
from discord.ext import tasks

intents = discord.Intents(messages=True, members=True, guilds=True)

# var
token = "token_line_15"
cid = "client_id_line_16"
owner = [
        "αrchιshα#5518",
        "notsniped#0002",
        "thatOneArchUser#5794"
]
oid = [
        "706697300872921088",
        "738290097170153472",
        "705462972415213588"
]

# prefix and status setup
bot = commands.Bot(command_prefix=']', intents=intents, activity=discord.Activity(type=discord.ActivityType.watching, name="everyone | ]help"), status=discord.Status.idle)
status = 'idle'

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == bot.user:
        return

# when ready
@bot.event
async def on_ready():
    print(f'\n> {bot.user} HAS CONNECTED TO DISCORD.\n\n> OWNER:\n')
    for i in owner:
        print(f"{i}\n")
    print("OWNER\'S ID:\n")
    for s in oid:
        print(f"{s}\n")

# error handler
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Missing required argument.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have the permission to do that. :eyes:")

# join dm
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.mention}, welcome to my testing server!'
    )

# help cmd
bot.remove_command('help')

@bot.command(aliases=['help'])
async def embed(ctx):
    embed=discord.Embed(title="**help command list of iso6.9**", description="current version: 13122021a\ncurrent prefix: `]`", 
    color=discord.Color.blue())
    embed.add_field(name='moderation:', value="kick, ban, unban, purge, mute, unmute, warn", inline=False)
    embed.add_field(name='bot info:', value="testcmd, ping, serverlist, otherbots, serverinfo, userinfo", inline=False)
    embed.add_field(name='misc:', value="snipe (channel), edit_snipe (global), 8ball, fstab, roll, say, null, quote, sus, notify", inline=False)
    embed.add_field(name='disabled:', value="<no commands>", inline=False)
    embed.set_footer(text="> type ]help to get this list.\n(Information requested by: {})".format(ctx.author.display_name))
    await ctx.send(embed=embed)

# cmds
@bot.command(aliases=['testcmd'])
async def testresp(ctx):
    ranresponse = [
        'hi! i\'m isobot but from different creator!',
        'e!'
    ]
    response = random.choice(ranresponse)
    await ctx.send(response)

@bot.command()
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = [
            "no?????",
            "When you grow a braincell, yes",
            "You stupid, of course not",
            "lol no",
            "Absolutely!",
            "Bet on it",
            "As I see it, yes.",
            "Most likely.",
            "Yes.",
            "Idfk",
            "Try again",
            "Not today.",
            "I\'m not very sure, but I think the answer is no.",
            "I\'m not very sure, but I think the answer is yes!",
            "brain.exe stopped responding.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Its a secret :>"
    ]
    ballEmbed= discord.Embed(title=f':8ball: {question}', description=f'{random.choice(responses)}')
    await ctx.send(embed=ballEmbed)

@bot.command()
async def ping(ctx):
        await ctx.send(f'Client Latency: {round(bot.latency * 1000)}ms')

# fstab var
fstaburl1 = "https://cdn.discordapp.com/attachments/878297190576062515/879845618636423259/IMG_20210825_005111.jpg"
fstaburl2 = "https://media.discordapp.net/attachments/876826249820004385/884040441195003954/Screenshot_158.png"
fstaburl3 = "https://media.discordapp.net/attachments/915898952182796298/916626889165115422/Screenshot_2017-10-10-01-22-57_com.speedsoftware.explorer_1507591405249.jpg"
fstaburl4 = "https://media.discordapp.net/attachments/915898952182796298/916626889412599858/644b5b9e083e806173eabcde0b6b5f0c_720w.png"

@bot.command()
async def fstab(ctx):
    fstabimg = [
            fstaburl1,
            fstaburl2,
            fstaburl3,
            fstaburl4
    ]
    fstabresp = random.choice(fstabimg)
    await ctx.send(fstabresp)

# slist var
archlink = "<https://discord.gg/aw4AcZys6p>"
smlink = "<https://discord.gg/tJqDMucEYG>"
isolink = "<https://discord.gg/zTqZqQCcAg>"

@bot.command(aliases=["serverlist", "slist"])
async def embed_2(ctx):
    embed=discord.Embed(title="**server list**", description="~~(101% not advertising)~~", color=0xFF5733)
    embed.add_field(name=f"1. Arch Island (aka Hecker\'s Hub\):", value=f"{archlink}", inline=False)
    embed.add_field(name=f"2. Scope Media (aka SM\):", value=f"{smlink}", inline=False)
    embed.add_field(name=f"3. iso.bot (aka isobot\'s supporting server\):", value=f"{isolink}", inline=False)
    await ctx.send(embed=embed)

# bots var
archbot = "https://discord.com/api/oauth2/authorize?client_id=859869941535997972&permissions=8&scope=bot"
isobot = "https://discord.com/api/oauth2/authorize?client_id=896437848176230411&permissions=8&scope=bot"
isobot2 = "https://discord.com/oauth2/authorize?client_id=915488087554002956&permissions=8&scope=bot"

@bot.command(aliases=["morebots", "bots"])
async def embed_3(ctx):
    embed=discord.Embed(title="**Discover more bots!**", description="~~(101% not advertising)~~", color=0xFF5733)
    embed.add_field(name=f"1. Arch bot#6142 (aka Archbot\):", value=f"{archbot}", inline=False)
    embed.add_field(name=f"2. isobot#6851 (aka Official isobot\):", value=f"{isobot}", inline=False)
    embed.add_field(name=f"3. iso6.9#4895 (aka isobot v6.9\):", value=f"{isobot2}", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def say(ctx, *, text):
    await ctx.message.delete()
    await ctx.send(f'{text}')

@bot.command(aliases=["null"])
async def null_1(ctx):
    zero = [
            "Oh so you want a **null**? Here you are: ",
            "You got **null**! Congratulations!",
            "Ok here is your **null**, enjoy!",
            "**null**.",
            "Well, you don\'t know what is null? Here is your **null**..."
    ]
    nullresp = random.choice(zero)
    await ctx.send(nullresp)

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has kicked successfully.')

@bot.command(pass_context=True, aliases=['purge', 'clear'])
@commands.has_permissions(administrator=True)
async def clean(ctx, limit: int):
    await ctx.channel.purge(limit=limit)
    await ctx.send('Cleared by {}'.format(ctx.author.mention))
    await ctx.message.delete()
@clean.error
async def clear_error(ctx,error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You can not do that!")

@bot.command(aliases=['shutup'])
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    embed = discord.Embed(title="muted", description=f"{member.mention} was muted successfully.", colour=discord.Colour.light_gray())
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f" you have been muted from: {guild.name}\n reason: {reason}")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

   await member.remove_roles(mutedRole)
   await member.send(f" you have unmuted from: - {ctx.guild.name}")
   embed = discord.Embed(title="unmute", description=f" unmuted-{member.mention}",colour=discord.Colour.light_gray())
   await ctx.send(embed=embed)

# quote var
quote1 = "i use arch btw."
author1 = "thatOneArchUser#5794"
quote2 = "we all playing systemd."
author2 = "notsniped#0002"
quote3 = "isobot is evolving, but backwards."
author3 = "αrchιshα#5518"

@bot.command(name="quote")
async def quote_1(ctx):
    quoted = [
            f"> \"{quote1}\" - {author1}",
            f"> \"{quote2}\" - {author2}",
            f"> \"{quote3}\" - {author3}"
    ]
    quoteresp = random.choice(quoted)
    await ctx.send(quoteresp)

@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send(f'User {member} has been banned successfully.')

@bot.command()
async def unban(ctx, id: int):
    user = await bot.fetch_user(id)
    await ctx.guild.unban(user)

# snipe
snipe_message_author = {}
snipe_message_content = {}

@bot.event
async def on_message_delete(message):
    snipe_message_author[message.channel.id] = message.author
    snipe_message_content[message.channel.id] = message.content
    await asyncio.sleep(60)
    del snipe_message_author[message.channel.id]
    del snipe_message_content[message.channel.id]

@bot.command()
async def snipe(ctx):
    channel = ctx.channel
    try:
        em = discord.Embed(title = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id])
        em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}")
        await ctx.send(embed = em)
    except:
        await ctx.send(f"There are no recently deleted messages in #{channel.name}")
# end of snipe

# edit_snipe
@bot.event
async def on_message_edit(message_before, message_after):
    if not message_after.author.bot:
        global author
        author = message_before.author
        guild = message_before.guild.id
        channel = message_before.channel
        global before
        before = message_before.content
        global after
        after = message_after.content
    else:
        pass

@bot.command()
async def edit_snipe(ctx):
    try:
        em = discord.Embed(description=f'**Message before**: {before}\n**Message after**:{after}')
        em.set_footer(text=f'This message was edited by {author}')
        await ctx.send(embed = em)
    except:
        await ctx.reply('No recent edited messages here :eyes:')
# end of edit_snipe

@bot.command(aliases=['sinfo'])
async def serverinfo(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)
    gowner = str(ctx.guild.owner)
    gid = str(ctx.guild.id)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)
   
    embed = discord.Embed(
        title=name + " Server Information",
         description=description,
         color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=gowner, inline=True)
    embed.add_field(name="Server ID", value=gid, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)

@bot.command(aliases=['whois'])
async def userinfo(ctx, *, member:discord.Member = None):
    if member == None:
            member = ctx.message.author

    embed=discord.Embed(
        title="User Information", 
        timestamp=datetime.utcnow(),
        color=discord.Color.random()
    )
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="Username:", value=member.name, inline=False)
    embed.add_field(name="Nickname (Displayed Name As):", value=member.nick, inline=False)
    embed.add_field(name="User ID:", value=member.id, inline=False)
    embed.add_field(name="Account Created At:",value=member.created_at.strftime("%a %#d %B %Y, %I:%M %p UTC"), inline=False)
    embed.add_field(name="Joined Server At:",value=member.joined_at.strftime("%a %#d %B %Y, %I:%M %p UTC"), inline=False)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def warn(ctx, user:discord.User = None, *, warn_reason=None):
    if user == None:
        await ctx.reply('Please mention a user when you want to warn someone next time.')
        return
    try:
        if warn_reason == None:
            warn_reason = '*Not provided*'
        embed67 = discord.Embed(title=f'You were warned in {ctx.guild}.', description=f'Reason: {warn_reason}', color=discord.Color.blue())
        await user.send(embed = embed67)
        embed70 = discord.Embed(title=f':white_check_mark: I successfully warned **{user}**.', color=discord.Color.green())
        await ctx.send(embed = embed70)
    except:
        embed71 = discord.Embed(title=f':x: Hold up!', description=f'I was unable to warn {user}.\nThis is usually caused due to the user not accepting DMs.', color=discord.Color.red())
        await ctx.send(embed = embed71)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def notify(ctx, user:discord.User = None, *, message):
    if user == None:
        await ctx.reply('If you want to notify a user, you need to ping someone.')
        return
    embed64 = discord.Embed(title=f'{ctx.message.author} notified you!', description=f'Message: {message}', color=discord.Color.blue())
    await user.send(embed = embed64)
    embed61 = discord.Embed(title=f':white_check_mark: I notified **{user}**', description=f'Message content: {message}', color=discord.Color.green())
    await ctx.channel.send(embed = embed61)

@bot.command(aliases=['sus'])
async def isSus(ctx, *, user : discord.User):
    susvar = [
        True,
        False
    ]
    sus = random.choice(susvar)
    if bool(sus) == True:
        await ctx.send(f'{user.mention} is very sus')
    elif bool(sus) == False:
        await ctx.send(f'{user.mention} isn\'t sus')
    else:
        await ctx.reply('undefined')

# start
bot.run(token)
