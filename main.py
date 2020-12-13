import os
import discord
from discord.ext import commands
import json
import datetime


with open('./config/config.json', 'r') as cjson:
    config = json.load(cjson)

client = commands.Bot(command_prefix=config["prefix"], case_insensitive=True)
client.remove_command('help')
client.author_id = config["dev"] 
client.config = config

start_time = datetime.datetime.now()

def timedelta_str(dt):
    """time uptime"""
    days = dt.days
    hours, r = divmod(dt.seconds, 3600)
    minutes, sec = divmod(r, 60)

    if minutes == 1 and sec == 1:
        return '{0} days, {1} hours, {2} minute and {3} second.'.format(days,hours,minutes,sec)
    elif minutes > 1 and sec == 1:
        return '{0} days, {1} hours, {2} minutes and {3} second.'.format(days,hours,minutes,sec)
    elif minutes == 1 and sec > 1:
        return '{0} days, {1} hours, {2} minute and {3} seconds.'.format(days,hours,minutes,sec)
    else:
        return '{0} days, {1} hours, {2} minutes and {3} seconds.'.format(days,hours,minutes,sec)

@client.command()
async def uptime(ctx):
    """Displays bot uptime."""
    global start_time
    await ctx.send(timedelta_str(datetime.datetime.now() - start_time))

@client.command()
async def help(ctx):
    """help command bot"""
    
    embed = discord.Embed(title='help sug', color=0xDCFF00)
    embed.add_field(name='{}sug'.format(client.command_prefix), value='To send a suggestion', inline=False)
    embed.add_field(name='{}uptime'.format(client.command_prefix), value='time uptime bot', inline=False)
    await ctx.send( embed = embed )



for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')





if __name__ == "__main__":
    if config["token"] == "":
        client.run(os.environ['token'])
    else:    
	    client.run(config["token"])


# All rights reserved © HazemMeqdad 2020
# Contact with me: https://discordapp.com/channels/@me/740700552593145876
