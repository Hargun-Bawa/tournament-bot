import discord
from discord.ext import commands
from config import TOKEN

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    print('------')

if __name__ == '__main__':
    bot.run(TOKEN)