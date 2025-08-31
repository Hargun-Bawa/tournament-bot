# This example requires the 'message_content' intent.
import discord
from config import TOKEN
import cogs.tournament
import datetime 
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
cog = cogs.tournament.TournamentApp(client)
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):


    if message.author == client.user:
        return
    elif message.content.startswith('$hello') and message.author.guild_permissions.administrator:
        date_name = create_unique_folder(datetime.datetime.now().strftime("%d %B %Y"))
        cogs.name = date_name
        os.makedirs(date_name)
        await cog.hello(cog, message.channel)

    elif message.content.startswith('$in'):
        await cog.selfAdd(cog, message.channel, message.author)

    elif message.content.startswith("$add"):
        for m in message.mentions:
            await cog.modAdd(cog, message.channel, m)
    elif message.contents.startswith("$start"):
        cogs.rounds = 1


    elif message.content.startswith("$report"):
        await cog.selfReport(cog, message.channel, message.author, message.content)
    

def create_unique_folder(folder_name):
    base_folder = f"tourney_{folder_name}"

    # Check if the base folder exists
    if os.path.exists(base_folder):
        # Increment the counter and append to the base folder name
        counter = 1
        while True:
            new_folder = f"{base_folder}_{counter}"
            if not os.path.exists(new_folder):
                break
            counter += 1
        return new_folder
    else:
        return base_folder

client.run(TOKEN)