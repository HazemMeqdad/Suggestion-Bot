import discord
from discord.ext import commands
import json



class sug(commands.Cog):
    def __init__(self, client, config):
        self.client = client
        self.config = config
    


    @commands.command(aliases=['suggestion', 'اقتراح'])
    async def sug(self, ctx,* , sugg):
        """suggestion comamnd"""
        channel = self.client.get_channel(self.config['channel'])
        await ctx.message.delete()
        embed = discord.Embed(title='New Suggestion By {}'.format(ctx.author.display_name))
        embed.add_field(name='Suggestion: ', value=sugg)
        embed.set_footer(text='UserID: ( {} ) | sID: ( {} )'.format(ctx.author.id, ctx.author.display_name), icon_url=ctx.author.avatar_url)
        suggg = await channel.send(embed=embed)
        
        embed = discord.Embed(description='☑️ Your Suggestion Has Been Sent To <#{}> !'.format(channel.id))
        embed.set_image(url='https://images-ext-2.discordapp.net/external/b-FNTxto_ItLGw2S8DkU0BXyzhpWMD45gb3Y3wZpXXQ/http/i8.ae/94Xd5')
        await ctx.send(embed = embed)
        await suggg.add_reaction("👍")
        await suggg.add_reaction("👎")

    @sug.error
    async def _sug_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.message.delete()
            embed = discord.Embed(color=0xFF2E00)
            embed.add_field(name='{}sug'.format(self.client.command_prefix), value='{}sug <message>'.format(self.client.command_prefix), inline=False)
            embed.add_field(name='{}اقتراح'.format(self.client.command_prefix), value='{}اقتراح <message>'.format(self.client.command_prefix), inline=False)
            embed.add_field(name='{}suggestion'.format(self.client.command_prefix), value='{}suggestion <message>'.format(self.client.command_prefix), inline=False)
            await ctx.send( embed = embed )	



def setup(client):
    client.add_cog(sug(client, client.config))