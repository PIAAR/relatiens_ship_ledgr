# backend/utils/cache_utils.py

from db import redis_client
import json

def cache_crystal_result(user_id: str, data: dict, ttl: int = 86400):
    key = f"crystal_profile:{user_id}"
    redis_client.setex(key, ttl, json.dumps(data))

def get_cached_crystal_result(user_id: str):
    key = f"crystal_profile:{user_id}"
    data = redis_client.get(key)
    return json.loads(data) if data else None
