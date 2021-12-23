# modules
import random
import discord
import asyncio
import datetime
import time
import cmath
import math
import string


from datetime import datetime
from random import randint
from discord.ext import commands
from discord.ext.commands import *

intents = discord.Intents(messages=True, members=True, guilds=True)

# var
token = "token"
cid = "client_id"
owner = [
        "αrchιshα#5518",
        "notsniped#0002",
        "thatOneArchUser#5794"
]
oid = [
        706697300872921088,
        738290097170153472,
        705462972415213588
]

# prefix and status setup
bot = commands.Bot(command_prefix=']', intents=intents)

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
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"everyone in {str(len(bot.guilds))} guilds | ]help"))
    print('[log] Log is loading...')
    print(f'[log] {bot.user} changed its activity.')

@bot.event
async def on_guild_join(guild):
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"everyone in {str(len(bot.guilds))} guilds | ]help"))
    print(f'[log] {bot.user} changed its activity.')

@bot.event
async def on_guild_remove(guild):
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"everyone in {str(len(bot.guilds))} guilds | ]help"))
    print(f'[log] {bot.user} changed its activity.')
# end of startup

# error handler
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Missing required argument(s).')
        print(f'[log] {ctx.author} returned an error: {error}.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have the permission to do that. :eyes:")
        print(f'[log] {ctx.author} returned an error: {error}.')
    if isinstance(error, BotMissingPermissions):
        await ctx.send('I don\'t have the required permissions to use this.')
        print(f'[log] {ctx.author} returned an error: {error}.')
    if isinstance(error, BadArgument):
        await ctx.send('Invalid argument')
        print(f'[log] {ctx.author} returned an error: {error}.')
    if isinstance(error, commands.CommandOnCooldown):
        if math.ceil(error.retry_after) < 60:
            await ctx.reply(f'This command is on cooldown. Please try after {math.ceil(error.retry_after)} seconds')
            print(f'[log] {ctx.author} returned an error: {error}.')
        elif math.ceil(error.retry_after) < 3600:
            ret = math.ceil(error.retry_after) / 60
            await ctx.reply(f'This command is on cooldown. Please try after {math.ceil(ret)} minutes')
            print(f'[log] {ctx.author} returned an error: {error}.')
        elif math.ceil(error.retry_after) >= 3600:
            ret = math.ceil(error.retry_after) / 3600
            if ret >= 24:
                r = math.ceil(ret) / 24
                await ctx.reply(f"This command is on cooldown. Please try after {r} days")
                print(f'[log] {ctx.author} returned an error: {error}.')
            else:
                await ctx.reply(f'This command is on cooldown. Please try after {math.ceil(ret)}')
                print(f'[log] {ctx.author} returned an error: {error}.')
            # How to use cooldowns:
            # after @bot.command() add @commands.cooldown(1, cooldown, commands.BucketType.user)
# end of error handler

# help cmd
bot.remove_command('help')

@bot.command(aliases=['help'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def embed(ctx):
    embed=discord.Embed(title="**help command list of iso6.9**", description="current version: 23122021b\ncurrent prefix: `]`", color=discord.Color.blue())
    embed.add_field(name='moderation:', value="kick, ban, unban, purge, mute, unmute, warn, lock, unlock", inline=False)
    embed.add_field(name='informative:', value="testcmd, ping, serverlist, morebots, serverinfo, userinfo", inline=False)
    embed.add_field(name='misc:', value="snipe (channel), edit_snipe (global), 8ball, fstab, roll, say, null, sus, notify, stroke, randnum, kill, amogus, guess, duel", inline=False)
    embed.add_field(name='mathematics:', value="sum, subtract, multiply, divide, power, squareroot", inline=False)
    embed.add_field(name='advanced maths:', value="quadratic, straightline", inline=False)
    embed.add_field(name='administrator:', value="> use `sudo help` to get details about admin commands.", inline=False)
    embed.set_footer(text="> type ]ahelp to get alias list.\n(Information requested by: {})".format(ctx.author))
    await ctx.reply(embed=embed)
    print(f'[log] {ctx.author} requested ]help.')

@bot.command(aliases=['ahelp'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def embed77(ctx):
    embed=discord.Embed(title='**alias list of iso6.9**', description='> use aliases to shorten commands', color=discord.Color.blue())
    embed.add_field(name='moderation:', value='kick, ban, unban, clear, shutup, unmute, warn, lock, unlock', inline=False)
    embed.add_field(name='informative:', value="test, ping, slist, bots, sinfo, whoami", inline=False)
    embed.add_field(name='misc:', value="snipe (channel), edit_snipe (global), 8ball, fstab, roll, say, null, sus, notify, stroke, randgen, kill, amogus, guess, duel", inline=False)
    embed.add_field(name='mathematics:', value="+, -, *, /, **, sqrt", inline=False)
    embed.add_field(name='advanced maths:', value="quad, stline", inline=False)
    embed.add_field(name='administrator:', value="> use `sudo help` to get details about admin commands.", inline=False)
    embed.set_footer(text='> type ]help to get the original list.\n(Information requested by: {})'.format(ctx.author))
    await ctx.reply(embed=embed)
    print(f'[log] {ctx.author} requested ]ahelp.')

# sudo
@bot.event
async def on_message(message):
    embed=discord.Embed(title='**admin command list of iso6.9**', description='admin prefix: `sudo\{space\}`', color=discord.Color.green())
    embed.add_field(name='control:', value='shutdown', inline=False)
    embed.set_footer(text='you\'re an admin, wow')
    await bot.process_commands(message) # add this if you're also using cmd decorators
    
    if message.content.startswith("sudo help") and not message.author.bot:
        if message.author.id in oid:
            await message.reply(embed=embed)
            print(f'[{message.author.name}@iso6.9 ~] requested sudo command.')
        else:
            await message.reply(f'{message.author.name} you are not an admin!')
            print(f'[log] Beware! Non-admin using sudo command detected. Requested by: {message.author.name}')
    
    if message.content.startswith("sudo shutdown") and not message.author.bot:
        if message.author.id in oid:
            await message.reply("Shutting down...", mention_author=False)
            print(f'[{message.author.name}@iso6.9 ~] SystemExit triggered in sudo command.')
            raise SystemExit("Bot shutdown triggered")
        else:
            await message.reply("no")
            print(f'[log] {message.author.name} returned an error: User not admin.')

# cmds
@bot.command(aliases=['test'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def testcmd(ctx):
    ranresponse = [
        'this is a test command',
        'did u just used ]test?'
    ]
    response = random.choice(ranresponse)
    await ctx.send(response)
    print(f'[log] {ctx.author} requested ]test.')

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))
    print(f'[log] {ctx.author} requested ]roll.')

@bot.command(aliases=['8ball'])
@commands.cooldown(1, 5, commands.BucketType.user)
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
    ballEmbed = discord.Embed(title=f':8ball: {question}', description=f'{random.choice(responses)}')
    await ctx.send(embed=ballEmbed)
    print(f'[log] {ctx.author} requested ]8ball.')

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def ping(ctx):
    await ctx.send(f'Client Latency: {round(bot.latency * 1000)}ms')
    print(f'[log] {ctx.author} requested ]ping.')

# fstab var
fstaburl1 = "https://cdn.discordapp.com/attachments/878297190576062515/879845618636423259/IMG_20210825_005111.jpg"
fstaburl2 = "https://media.discordapp.net/attachments/876826249820004385/884040441195003954/Screenshot_158.png"
fstaburl3 = "https://media.discordapp.net/attachments/915898952182796298/916626889165115422/Screenshot_2017-10-10-01-22-57_com.speedsoftware.explorer_1507591405249.jpg"
fstaburl4 = "https://media.discordapp.net/attachments/915898952182796298/916626889412599858/644b5b9e083e806173eabcde0b6b5f0c_720w.png"

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def fstab(ctx):
    fstabimg = [
            fstaburl1,
            fstaburl2,
            fstaburl3,
            fstaburl4
    ]
    fstabresp = random.choice(fstabimg)
    await ctx.send(fstabresp)
    print(f'[log] {ctx.author} requested ]fstab.')

# slist var
archlink = "<https://discord.gg/aw4AcZys6p>"
smlink = "<https://discord.gg/tJqDMucEYG>"
isolink = "<https://discord.gg/zTqZqQCcAg>"

@bot.command(aliases=["serverlist", "slist"])
@commands.cooldown(1, 5, commands.BucketType.user)
async def embed_2(ctx):
    embed=discord.Embed(title="**server list**", description="~~(101% not advertising)~~", color=0xFF5733)
    embed.add_field(name=f"1. Arch Island (aka Hecker\'s Hub\):", value=f"{archlink}", inline=False)
    embed.add_field(name=f"2. Scope Media (aka SM\):", value=f"{smlink}", inline=False)
    embed.add_field(name=f"3. iso.bot (aka isobot\'s supporting server\):", value=f"{isolink}", inline=False)
    await ctx.send(embed=embed)
    print(f'[log] {ctx.author} requested ]serverlist.')

# bots var
archbot = "https://discord.com/api/oauth2/authorize?client_id=859869941535997972&permissions=8&scope=bot"
isobot = "https://discord.com/api/oauth2/authorize?client_id=896437848176230411&permissions=8&scope=bot"
isobot2 = "https://discord.com/oauth2/authorize?client_id=915488087554002956&permissions=8&scope=bot"

@bot.command(aliases=["morebots", "bots"])
@commands.cooldown(1, 5, commands.BucketType.user)
async def embed_3(ctx):
    embed=discord.Embed(title="**Discover more bots!**", description="~~(101% not advertising)~~", color=0xFF5733)
    embed.add_field(name=f"1. Arch bot#6142 (aka Archbot\):", value=f"{archbot}", inline=False)
    embed.add_field(name=f"2. isobot#6851 (aka Official isobot\):", value=f"{isobot}", inline=False)
    embed.add_field(name=f"3. iso6.9#4895 (aka isobot v6.9\):", value=f"{isobot2}", inline=False)
    await ctx.send(embed=embed)
    print(f'[log] {ctx.author} requested ]morebots.')

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def say(ctx, *, text):
    await ctx.message.delete()
    await ctx.send(f'{text}')
    print(f'[log] {ctx.author} requested ]say, content: {ctx.message_content}.')

@bot.command(aliases=["null"])
@commands.cooldown(1, 5, commands.BucketType.user)
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
    print(f'[log] {ctx.author} requested ]null.')

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has kicked successfully.')
    print(f'[log] {ctx.author} requested ]kick.')

@bot.command(pass_context=True, aliases=['purge', 'clear'])
@commands.cooldown(1, 10, commands.BucketType.user)
@commands.has_permissions(administrator=True)
async def clean(ctx, limit: int):
    await ctx.channel.purge(limit=limit)
    print(f'[log] {ctx.author} requested ]purge.')
    await ctx.send('Cleared by {}'.format(ctx.author.mention))
    await ctx.message.delete()
@clean.error
async def clear_error(ctx,error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You can not do that!")
        print(f'[log] {ctx.author} returned an error: {error}.')

@bot.command(aliases=['shutup'])
@commands.cooldown(1, 10, commands.BucketType.user)
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
    print(f'[log] {ctx.author} requested ]mute.')
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f" you have been muted from: {guild.name}\n reason: {reason}")
    print(f'[log] {ctx.author} \'s DM has successfully sent.')

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

   await member.remove_roles(mutedRole)
   await member.send(f" you have unmuted from: - {ctx.guild.name}")
   print(f'[log] {ctx.author} \'s DM has successfully sent.')
   embed = discord.Embed(title="unmute", description=f" unmuted-{member.mention}",colour=discord.Colour.light_gray())
   await ctx.send(embed=embed)
   print(f'[log] {ctx.author} requested ]unmute.')

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send(f'User {member} has been banned successfully.')
    print(f'[log] {ctx.author} requested ]ban.')

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def unban(ctx, id: int):
    user = await bot.fetch_user(id)
    await ctx.guild.unban(user)
    print(f'[log] {ctx.author} requested ]unban.')

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
@commands.cooldown(1, 5, commands.BucketType.user)
async def snipe(ctx):
    channel = ctx.channel
    try:
        em = discord.Embed(title = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id])
        em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}")
        await ctx.send(embed = em)
        print(f'[log] {ctx.author} requested ]snipe.')
    except:
        await ctx.send(f"There are no recently deleted messages in #{channel.name}")
        print(f'[log] {ctx.author} returned an error: No recently deleted messages.')
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
@commands.cooldown(1, 5, commands.BucketType.user)
async def edit_snipe(ctx):
    try:
        em = discord.Embed(description=f'**Message before**: {before}\n**Message after**:{after}')
        em.set_footer(text=f'This message was edited by {author}')
        await ctx.send(embed = em)
        print(f'[log] {ctx.author} requested ]edit_snipe.')
    except:
        await ctx.reply('No recently edited messages here :eyes:')
        print(f'[log] {ctx.author} returned an error: No recently edited messages.')
# end of edit_snipe

@bot.command(aliases=['sinfo'])
@commands.cooldown(1, 5, commands.BucketType.user)
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
    print(f'[log] {ctx.author} requested ]serverinfo.')

@bot.command(aliases=['whois'])
@commands.cooldown(1, 5, commands.BucketType.user)
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
    print(f'[log] {ctx.author} requested ]userinfo.')

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
@commands.has_permissions(manage_messages=True)
async def warn(ctx, user:discord.User = None, *, warn_reason=None):
    if user == None:
        await ctx.reply('Please mention a user when you want to warn someone next time.')
        print(f'[log] {ctx.author} returned an error: No user mentioned.')
        return
    try:
        if warn_reason == None:
            warn_reason = '*Not provided*'
        embed67 = discord.Embed(title=f'You were warned in {ctx.guild}.', description=f'Reason: {warn_reason}', color=discord.Color.blue())
        await user.send(embed = embed67)
        print(f'[log] {ctx.author} \'s DM has successfully sent.')
        embed70 = discord.Embed(title=f':white_check_mark: I successfully warned **{user}**.', color=discord.Color.green())
        await ctx.send(embed = embed70)
        print(f'[log] {ctx.author} requested ]warn.')
    except:
        embed71 = discord.Embed(title=f':x: Hold up!', description=f'I was unable to warn {user}.\nThis is usually caused due to the user not accepting DMs.', color=discord.Color.red())
        await ctx.send(embed = embed71)
        print(f'[log] {ctx.author} returned an error: DM not opened.')


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_permissions(manage_messages=True)
async def notify(ctx, user:discord.User = None, *, message):
    if user == None:
        await ctx.reply('If you want to notify a user, you need to mention someone.')
        print(f'[log] {ctx.author} returned an error: No user mentioned.')
        return
    embed64 = discord.Embed(title=f'{ctx.message.author} notified you!', description=f'Message: {message}', color=discord.Color.blue())
    await user.send(embed = embed64)
    print(f'[log] {ctx.author} \'s DM has successfully sent.')

    embed61 = discord.Embed(title=f':white_check_mark: I notified **{user}**', description=f'Message content: {message}', color=discord.Color.green())
    await ctx.channel.send(embed = embed61)
    print(f'[log] {ctx.author} requested ]notify, content: {ctx.message_content}.')

@bot.command(aliases=['sus'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def isSus(ctx, *, user: discord.User):
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
    print(f'[log] {ctx.author} requested ]sus.')

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel : discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    embed72 = discord.Embed(title='Channel locked successfully.')
    await ctx.send(embed=embed72)
    print(f'[log] {ctx.author} requested ]lock.')

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel : discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    embed73 = discord.Embed(title='Channel unlocked successfully.')
    await ctx.send(embed=embed73)
    print(f'[log] {ctx.author} requested ]unlock.')

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def stroke(ctx, size: int):
    def random_string_generator(str_size, allowed_chars):
        return ''.join(random.choice(allowed_chars) for x in range(str_size))
    chars = string.ascii_letters + string.punctuation

    if size > 550:
        await ctx.send(f'{size} is more than the limit. The max character limit is set to 550 to avoid spam.')
        print(f'[log] {ctx.author} returned an error: Max character limit reached.')
    else:
        await ctx.send(random_string_generator(size, chars))
        print(f'[log] {ctx.author} requested ]stroke.')

# maths cmds
@bot.command(aliases=['+'])
async def sum(ctx, num1: float, num2: float):
    ans = str(num1 + num2)
    await ctx.send(f'`{num1} + {num2}` = __{ans}__\n\n--end of calculation--')
    print(f'[log] {ctx.author} requested ]sum.')

@bot.command(aliases=['-'])
async def subtract(ctx, num1: float, num2:float):
    ans = str(num1 - num2)
    await ctx.send(f'`{num1} - {num2}` = __{ans}__\n\n--end of calculation--')
    print(f'[log] {ctx.author} requested ]subtract.')

@bot.command(aliases=['*'])
async def multiply(ctx, num1: float, num2: float):
    ans = str(num1 * num2)
    await ctx.send(f'`{num1} × {num2}` = __{ans}__\n\n--end of calculation--')
    print(f'[log] {ctx.author} requested ]multiply.')

@bot.command(aliases=['/'])
async def divide(ctx, num1: float, num2: float):
    if num2 == 0:
        await ctx.send("math error: it can\'t be divided by zero.")
        print(f'[log] {ctx.author} returned an math error: Divide by zero.')
        return
    ans = str(num1 / num2)
    await ctx.send(f'`{num1} ÷ {num2}` = __{ans}__\n\n--end of calculation--')
    print(f'[log] {ctx.author} requested ]divide.')

@bot.command(aliases=['**'])
async def power(ctx, num1: float, num2: int):
    ans = str(num1 ** num2)
    await ctx.send(f'`{num1} ^ {num2}` = __{ans}__\n\n--end of calculation--')
    print(f'[log] {ctx.author} requested ]power.')

@bot.command(aliases=['sqrt'])
async def squareroot(ctx, num: float):
    ans = cmath.sqrt(num)
    await ctx.send(f'`√ {num}` = __{ans}__\n\n--end of calculation--')
    print(f'[log] {ctx.author} requested ]squareroot.')

@bot.command(aliases=['quad'])
async def quadratic(ctx, a: float, b: float, c: float):
    delta = (b**2) - (4*a*c)
    r1 = (-b+cmath.sqrt(delta)) / (2*a)
    r2 = (-b-cmath.sqrt(delta)) / (2*a)
    await ctx.send(f'The roots of `({a})x^(2)+({b})x+({c})` are __{r1}__ and __{r2}__\n\n--end of calculation--')
    print(f'[log] {ctx.author} requested ]quadratic.')

@bot.command(aliases=['stline'])
async def straightline(ctx, A: float, B: float, C: float):
    x = -C / A
    y = -C / B
    m = -A / B
    await ctx.send(f'x-intercept = __{x}__\ny-intercept = __{y}__\nslope of straight line= __{m}__\n\n--end of calculation--')
    print(f'[log] {ctx.author} requested ]straightline.')
# end of maths

@bot.command(aliases=['randgen'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def randnum(ctx, range1: int, range2: int):
    num = random.randint(range1, range2)
    await ctx.send(f'{num} is being picked.')
    print(f'[log] {ctx.author} requested ]randnum.') 

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def kill(ctx, user: discord.User, weapon: str):
    await ctx.send(f'{ctx.author} killed {user} with {weapon}, ouch.')
    print(f'[log] {ctx.author} requested ]kill.')

@bot.command()
async def amogus(ctx):
    await ctx.reply("https://c.tenor.com/1iSARWJr-TEAAAAC/among-us-twerk.gif")
    print(f'[log] {ctx.author} requested ]amogus.')

@bot.command()
async def guess(ctx, num: int):
    rand = random.randint(1, 9)
    if num == rand:
        await ctx.reply(f'Your choice is {num}, you guessed it right!')
    else: 
        await ctx.reply(f'Your choice is {num}, wrong!\nMy choice is {rand}.')
    print(f'[log] {ctx.author} requested ]guess.')

# duel
@bot.command()
async def duel(ctx, player2: discord.User):
# var
    normal = [
            # normal atk
            'Eclipse',
            'Magic Attack',
            'Power Burst',
            'Dragon Slayer',
            'Time Stealer' 
    ]
    special = [
            # special atk
            'Arch Strike',
            'Arch Morph',
            'Arch Aptitude',
            'Fstab',
            'Sudo Attack'
    ]
#
    def boolrnd():
        b1 = random.randint(1, 2)
        return b1

    definer1 = boolrnd()
    definer2 = boolrnd()
    definer3 = boolrnd()
    definer4 = boolrnd()

    if definer1 == 1:
        pick1 = random.choice(special)
    elif definer1 == 2:
        pick1 = random.choice(normal)
    if definer2 == 1:
        pick2 = random.choice(special)
    elif definer2 == 2:
        pick2 = random.choice(normal)
    if definer3 == 1:
        pick3 = random.choice(special)
    elif definer3 == 2:
        pick3 = random.choice(normal)
    if definer4 == 1:
        pick4 = random.choice(special)
    elif definer4 == 2:
        pick4 = random.choice(normal)

    round1 = pick1
    round2 = pick2
    round3 = pick3
    round4 = pick4
#
    def rnd1():
        r1 = random.randint(0, 60)
        return r1
    def rnd2():
        r2 = random.randint(30, 100)
        return r2
#
    if round1 in normal:
        hplost1 = rnd1()
    elif round1 in special:
        hplost1 = rnd2()
    if round2 in normal:
        hplost2 = rnd1()
    elif round2 in special:
        hplost2 = rnd2()
    if round3 in normal:
        hplost3 = rnd1()
    elif round3 in special:
        hplost3 = rnd2()
    if round4 in normal:
        hplost4 = rnd1()
    elif round4 in special:
        hplost4 = rnd2()

        lose1 = hplost1
        lose2 = hplost2
        lose3 = hplost3
        lose4 = hplost4
#
    hplast1 = 100 - lose2 - lose4
    hplast2 = 100 - lose1 - lose3
#
    if hplast1 > hplast2:
        winner = ctx.author
    elif hplast1 < hplast2:
        winner = player2
    elif hplast1 == hplast2:
        winner = "No one"
    else:
        winner = "undefined"
#
    await ctx.send(f'{ctx.author} used {round1}, dealt {lose1}!')
    await ctx.send(f'{player2} used {round2}, dealt {lose2}!')
    await ctx.send(f'{ctx.author} used {round3}, dealt {lose3}!')
    await ctx.send(f'{player2} used {round4}, dealt {lose4}!')
    await ctx.send(f'{ctx.author}\'s hp: {hplast1}\n{player2}\'s hp: {hplast2}\n\n{winner} won!')
    print(f'[log] {ctx.author} requested ]duel with {player2}')
# end of duel

# start
bot.run(token)
