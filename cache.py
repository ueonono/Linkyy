import time

_cache = {}

def get_from_cache(key):
    value, expiry = _cache.get(key, (None, 0))
    if time.time() < expiry:
        return value
    return None

def set_cache(key, value, ttl=60):
    _cache[key] = (value, time.time() + ttl)

def clear_cache():
    _cache.clear()
