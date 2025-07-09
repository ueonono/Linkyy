def format_rank(rank):
    # Exemple : Gold II -> 🥇 Gold II
    icons = {"Gold": "🥇", "Silver": "🥈", "Bronze": "🥉", "Platinum": "💎", "Diamond": "🔷", "Champion": "🏆"}
    for key, icon in icons.items():
        if key in rank:
            return f"{icon} {rank}"
    return rank

def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{hours}h {minutes}m"
