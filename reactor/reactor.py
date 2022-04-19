import discord
from discord import reaction
from discord.message import Message
from redbot.core import commands

class Reactor(commands.Cog):
    """Reactor"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I can do stuff!")
        
    @commands.Cog.listener()
    async def on_message(self, message: Message):
        if message.author.bot:
            return
        if message.guild is None:
            return
        
        
        pass

def get_emoji_command_from_string(input: str):
    pass