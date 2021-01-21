import discord
from discord.ext import commands

class Credits(commands.Cog):

    def _init_(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Credits Module ready.')

    @commands.command() #Credits
    async def credits(self, ctx):
        await ctx.send('Creator: \n'
                        '- Alexander Lafontaine \n'
                        '\n'
                        'Co Creators: \n'
                        '- Robert \n'
                        '\n'
                        'Idea Suggesters: \n'
                        '- Pablo \n'
                        '\n'
                        'Image Designers \n'
                        '- Felipe https://www.instagram.com/frg_commissions/?hl=es \n')

def setup(client):
    client.add_cog(Credits(client))