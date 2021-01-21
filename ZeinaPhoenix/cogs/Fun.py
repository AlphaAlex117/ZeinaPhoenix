import discord
from discord.ext import commands
import random 

class Fun(commands.Cog):

    def _init_(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Fun Module ready.')

    @commands.command(aliases=['8ball', 'eightball']) #Magic 8 Ball game
    async def _8ball(self, ctx, *, question):
        responses = ['As I see it, yes.',
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                'Do not count on it.',
                'It is certain.',
                'It is decidedly so.',
                'Most likely.',
                'My reply is no.',
                'My sources say no.',
                'Outlook not so good.',
                'Outlook good.',
                'Reply hazy, try again.',
                'Signs point to yes.',
                'Very doubtful.',
                'Without a doubt.',
                'Yes.',
                'Yes – definitely.',
                'You may rely on it.']
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    @commands.command() #Rock Paper Scissor
    async def rps(self, ctx, *, player):
        cpu = random.choice(["scissors","rock","paper"])
        if player.lower() == ("scissors"): #Scissor
            if cpu == ("rock"):
                await ctx.send(f'I WIN\nYour Answer: {player}\nMy Answer: {cpu}')
            elif cpu == ("scissors"):
                await ctx.send(f'TIE\nYour Answer: {player}\nMy Answer: {cpu}')
            elif cpu == ("paper"):
                await ctx.send(f'YOU WIN\nYour Answer: {player}\nMy Answer: {cpu}')
                
        elif player.lower() == ("rock"): #Rock
            if cpu == ("paper"):
                await ctx.send(f'I WIN\nYour Answer: {player}\nMy Answer: {cpu}')
            elif cpu == ("rock"):
                await ctx.send(f'TIE\nYour Answer: {player}\nMy Answer: {cpu}')
            elif cpu == ("scissors"):
                await ctx.send(f'YOU WIN\nYour Answer: {player}\nMy Answer: {cpu}')
                
        elif player.lower() == ("paper"): #Paper
            if cpu == ("scissors"):
                await ctx.send(f'I WIN\nYour Answer: {player}\nMy Answer: {cpu}')
            elif cpu == ("paper"):
                await ctx.send(f'TIE\nYour Answer: {player}\nMy Answer: {cpu}')
            elif cpu == ("rock"):
                await ctx.send(f'YOU WIN\nYour Answer: {player}\nMy Answer: {cpu}')
                
        else:
            await ctx.send(f'Are you trying to cheat? Write scissors, rock or paper.')

def setup(client):
    client.add_cog(Fun(client))