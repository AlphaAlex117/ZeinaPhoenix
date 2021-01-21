import discord
from discord.ext import commands
import math 

class SciCalculator(commands.Cog):

    def _init_(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Scientific Calculator Module ready.')

    @commands.command()
    async def calc(self, ctx, *, num1, operation, num2):
        a = float(num1)
        b = float(num2)

        if operation == ('+'):
            addition = (a + b)
            await ctx.send(f'{addition}')

        elif operation == ('-'):
            subtraction = (a - b)
            await ctx.send(f'{subtraction}')
        
        elif operation == ('*'):
            multiplication = (a * b)
            await ctx.send(f'{multiplication}')

        elif operation == ('/'):
            division = (a / b)
            await ctx.send(f'{division}')

        else:
            await ctx.sent('I do not compute.')

def setup(client):
    client.add_cog(SciCalculator(client))