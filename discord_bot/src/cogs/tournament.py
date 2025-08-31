import discord
from discord.ext import commands
from . import player
import json
import matchmaking

class TournamentApp(commands.Cog):
    def __init__(self, bot):
        self.matchmaker = 1
        self.pairings_generator = 1
        self.players = []
        self.started = False
        self.name = ""
        self.timer = 30
        self.rounds = 1


    def player_search(self, id):
        for i in self.players:
            if i.id == id:
                return True
        return False

        

    @commands.command(name='new_tourney')
    async def hello(self, ctx):
        await ctx.send('select matchmaking type')

    @commands.command(name = "self_add")
    async def selfAdd(self, ctx, auth):

        if self.player_search(auth.id):
            await ctx.send(auth.name + " is already enrolled ")
        else:
            self.players.append(player.Player(auth.name, auth.id))
            await ctx.send(str(auth.name) + " added")

    @commands.command(name = "mod_add")
    async def modAdd(self, ctx, user):

        if(self.player_search(user.id)):
            await ctx.send(user.name + " is already enrolled")

        else:
            self.players.append(player.Player(user.name, user.id))
            await ctx.send(user.name + "added")

    @commands.command(name = "report")
    async def selfReport(self, ctx, auth, message):
        if(self.started):
            for p in self.players:
                if(p.name == auth.name):
                    p.record[p.name] = (message[7:]).strip()
                    await ctx.send("result recorded as " + p.record[p.name])
        else:
            await ctx.send("please wait for round to start")
        
    @commands.command(name = "start")
    async def startTourney(self, ctx):
        {"players": {}}


       


async def setup(bot):
    await bot.add_cog(TournamentApp(bot))