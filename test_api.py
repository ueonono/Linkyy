import os
import requests
from dotenv import load_dotenv

load_dotenv()
MARVEL_API_KEY = os.getenv('MARVEL_RIVALS_API_KEY')

pseudo = "ueono"
url_update = f"https://marvelrivalsapi.com/api/v1/player/{pseudo}/update"
url_info = f"https://marvelrivalsapi.com/api/v1/player/{pseudo}"
headers = {"x-api-key": MARVEL_API_KEY}

with open("api_test.log", "w", encoding="utf-8") as log:
    r = requests.get(url_update, headers=headers)
    log.write(f"Update status: {r.status_code}\nUpdate response: {r.text}\n\n")
    r = requests.get(url_info, headers=headers)
    log.write(f"Info status: {r.status_code}\nInfo response: {r.text}\n")

print("Test terminé. Voir api_test.log pour les résultats.")
