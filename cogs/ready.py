import discord
from discord.ext import commands


class ready(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        """event on ready"""
        activity = discord.Game(name=f"{self.client.command_prefix}sug", type=1)
        await self.client.change_presence(status=discord.Status.online, activity=activity)
        print('==================================================')
        print('online {}'.format(self.client.user.name))
        print('All rights reserved © HazemMeqdad 2020')
        print('==================================================')



def setup(client):
    client.add_cog(ready(client))