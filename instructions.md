# Marvel Rivals Discord Bot – Instructions de Mise en Place

## 1. Prérequis
- Python 3.9+
- Un bot Discord (token à créer sur https://discord.com/developers/applications)

## 2. Installation des dépendances
Dans le dossier du projet, exécutez :
```bash
pip install -r requirements.txt
```

## 3. Structure du projet
```
marvelink/
├── bot_discord.py
├── marvel_api.py
├── db.py
├── cache.py
├── utils.py
├── requirements.txt
├── instructions.md
├── cogs/
│   ├── hub.py
│   ├── profile.py
│   ├── matchmaking.py
│   ├── rating.py
│   ├── leaderboard.py
│   ├── xp.py
│   └── notifications.py
├── data/
```

## 4. Configuration
- Remplacez `VOTRE_TOKEN_DISCORD` dans `bot_discord.py` par le token de votre bot.
- Remplacez `ID_DU_CHANNEL_HUB` dans `cogs/hub.py` par l’ID du salon Discord qui servira de hub.

## 5. Lancement du bot
```bash
python bot_discord.py
```

## 6. Fonctionnalités principales
- 100% interactif (boutons, menus, aucune commande textuelle)
- Hub central, profils, matchmaking, notations, classements, XP, badges, notifications, comparaisons, podiums, défis quotidiens, etc.

## 7. Personnalisation
- Adaptez les cogs selon vos besoins.
- Ajoutez vos clés API Marvel Rivals dans `marvel_api.py` si nécessaire.

## 8. Conseils
- Utilisez SQLite pour stocker les profils, notations, XP, etc.
- Utilisez le système de cache pour limiter les appels API.
- Ajoutez des tâches planifiées pour les mises à jour automatiques.

---
Pour toute question, ouvrez une issue ou contactez le développeur principal.
