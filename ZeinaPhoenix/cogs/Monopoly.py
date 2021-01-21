import discord
from discord.ext import commands
import random 

class Monopoly(commands.Cog):

    def _init_(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Monopoly Module ready.')

    @commands.command()
    async def mlottery(self, ctx):
        number = random.randint(1, 100)
        await ctx.send(f'The lucky number is... {number}')

    @commands.command()
    async def mpolice(self, ctx):
        prison = random.choice(["caught", "not_caught"])
        caught = random.choice(["money", "not_money", "pay"])
        if prison == ("not_caught"):
            await ctx.send('You were not caught')
        elif prison == ("caught"):
            if caught == ("money"):
                await ctx.send('You will receive money from players')
            elif caught == ("not_money"):
                await ctx.send('You will not receive money from players')
            elif caught == ("pay"):
                await ctx.send('Pay the player $50')

def setup(client):
    client.add_cog(Monopoly(client))