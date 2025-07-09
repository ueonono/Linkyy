import aiohttp
import os

API_BASE_URL = "https://marvelrivalsapi.com/api/v1/player"
API_KEY = os.getenv("MARVEL_RIVALS_API_KEY")

async def update_player(pseudo):
    headers = {"x-api-key": API_KEY} if API_KEY else {}
    url = f"{API_BASE_URL}/{pseudo}/update"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as resp:
            return await resp.json() if resp.status == 200 else None

async def fetch_player_profile(pseudo):
    headers = {"x-api-key": API_KEY} if API_KEY else {}
    url = f"{API_BASE_URL}/{pseudo}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as resp:
            return await resp.json() if resp.status == 200 else None

# fetch_leaderboard reste à adapter selon l'API
