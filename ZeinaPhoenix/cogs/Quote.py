import discord
from discord.ext import commands
import random 

class Quote(commands.Cog):

    def _init_(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Quote Module ready.')

    @commands.command(aliases=['q']) #QUOTES JEJEJEJEJE
    async def quote(self, ctx, *, theme):
        if theme.lower() == ('star wars'):
            quotes = ['Hello there!',
                    'I don’t care what universe you’re from, that’s got to hurt!',
                    'Love won’t save you, Padme. Only my new powers can do that.',
                    'It’s over Anakin. I have the high ground!',
                    'You underestimate my power!',
                    'Don’t try it.',
                    'There’s always a bigger fish.',
                    'I don’t like sand. It’s coarse and rough and irritating and it gets everywhere.',
                    'I sense Count Dooku.',
                    'Ani? My goodness, you’ve grown!',
                    'UNLIMITED POWER!',
                    'So uncivilized.',
                    'Now this is pod racing!',
                    'So this is how liberty dies… with thunderous applause.',
                    'It is only natural. He cut off your arm, and you wanted revenge.',
                    'Always two there are, no more, no less.',
                    'From my point of view, the Jedi are evil!',
                    'Well, then you really are lost!',
                    'I have waited a long time for this moment, my little green friend.',
                    'I’ll try spinning. That’s a good trick.',
                    'I love democracy.',
                    'Your new Empire?',
                    'I have brought peace, freedom, justice, and security to my new empire.',
                    'This is the end for you my master.',
                    'I can’t watch anymore.']
            await ctx.send(f'{random.choice(quotes)}')
        elif theme.lower() == ('halo'):
            quotes = ['No, Sir.',
                    'Boo.',
                    'Thought I’d try shooting my way out- Mix things up a little.',
                    'I won’t.',
                    'No. I think we’re just getting started.',
                    'To give the covenant back their bomb.',
                    'Sir, finishing this fight.',
                    'She said that to me once. About being a machine.',
                    'Wake me when you need me.',
                    'Yes Sir, I need a weapon.',
                    ''''They let me pick, did I ever tell you that? Choose whichever Spartan I wanted.
                    You know me. I did my research. Watched as you became the soldier we needed you to be. 
                    Like the others, you were strong and swift and brave. A natural leader. But you had something they didn't. 
                    Something no one saw... but me. Can you guess? Luck. Was I wrong?''',
                    'Don’t let her go... don’t ever let her go.',
                    '''Men, keep your eyes downrange, fingers on the triggers, and we all come home in one piece. Am I right, Marines?''',
                    '''Once again, it is our job to finish what the flyboys started. We are leaving this ship's platoon, and engaging the Covenant on solid ground. 
                    When we meet the enemy, we will rip their skulls from their spines, and toss 'em away, laughin'! Am I right, Marines?''',
                    '''Men, we led those dumb bugs out to the middle of nowhere to keep 'em from gettin' their filthy claws on Earth.
                    But, we stumbled onto somethin' they're so hot for, that they're scramblin' over each other to get it. 
                    Well, I don't care if it's God's own anti-son-of-a-bitch machine, or a giant hula hoop, we're not gonna let 'em have it! 
                    What we will let 'em have is a belly full of lead, and a pool of their own blood to drown in! Am I right, Marines?''',
                    'Dear Humanity... We regret being alien bastards. We regret coming to Earth. And we most definitely regret that the Corps just blew up our raggedy-ass fleet!',
                    'You had your chance to be afraid before you joined my beloved Corps! But, to guide you back to the true path, I brought this motivational device! Our big green style cannot be defeated!',
                    'Usually, the good Lord works in mysterious ways. But not today! This here is 66 tons of straight-up, H.E-spewing dee-vine intervention! If God is love, then you can call me Cupid!']
            await ctx.send(f'{random.choice(quotes)}')
        elif theme.lower() == ('star trek'):
            quotes = [''
                    '']
            await ctx.send(f'{random.choice(quotes)}')
        elif theme.lower() == ('mass effect'):
            quotes = [''
                    '']
            await ctx.send(f'{random.choice(quotes)}')

def setup(client):
    client.add_cog(Quote(client))