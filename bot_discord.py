import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
HUB_CHANNEL_ID = os.getenv('HUB_CHANNEL_ID')
if HUB_CHANNEL_ID is not None:
    HUB_CHANNEL_ID = int(HUB_CHANNEL_ID)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)  # Préfixe inutilisé, mais requis par discord.py

# Chargement automatique des cogs
INITIAL_COGS = [
    'cogs.hub',
    'cogs.profile',
    'cogs.matchmaking',
    'cogs.rating',
    'cogs.leaderboard',
    'cogs.xp',
    'cogs.notifications'
]

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")

if __name__ == "__main__":
    if not DISCORD_TOKEN:
        raise RuntimeError("DISCORD_TOKEN manquant dans le .env")
    bot.run(DISCORD_TOKEN)
