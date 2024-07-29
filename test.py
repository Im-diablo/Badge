import os 
import discord
from discord import app_commands
from discord.ext import commands
import gdown

bot = commands.Bot(command_prefix="n", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.tree.command(name="ping")
async def ping(interaction: discord.Interaction):
  await interaction.response.send_message(f"Hey {interaction.user.mention}! This is a slash command!", ephemeral=True)

@bot.tree.command(name="sync")
@app_commands.describe(thing_to_say = "synced")
async def say(interaction: discord.Interaction, thing_to_say: str):
  await interaction.response.send_message(f"synced {interaction.user.mention} said: `{thing_to_say}`")
  
  url = 'https://drive.google.com/u/0/uc?id=1-rCeT404Do7m8Bu3cqXM6uYaniA661lB'
  output = 'token.txt'
  gdown.download(url, output, quiet=False)

  with open('token.txt') as f:
      TOKEN = f.readline()

bot.run(TOKEN)
