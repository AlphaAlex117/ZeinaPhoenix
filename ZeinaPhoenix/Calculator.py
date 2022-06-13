import discord
from discord.ext import commands
import math 

class SciCalculator(commands.Cog):

    #Initialization
    def _init_(self, client):
        self.client = client #client

        equation

    @commands.Cog.listener()
    async def on_ready(self):
        print('Scientific Calculator Module ready.')

    @commands.command()
    async def calc(self, ctx, *, premise):
        for x in premise:
            print(x)
            
    


def setup(client):
    client.add_cog(SciCalculator(client))