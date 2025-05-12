# backend/db.py

import os
from pymongo import MongoClient, errors
from config import MONGO_URI, REDIS_URL

# === MongoDB Setup ===
try:
    mongo_client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)  # 3s timeout
    mongo_db = mongo_client.get_database()
    # Test connection
    mongo_client.admin.command('ping')
    users_collection = mongo_db["users"]
    mbti_collection = mongo_db["mbti_results"]
    quiz_sessions_collection = mongo_db["quiz_sessions"]
    user_profile_collection = mongo_db["user_profiles"]
    print("[MongoDB] Connected successfully.")
except errors.ServerSelectionTimeoutError as e:
    print("[MongoDB] Connection failed. Using in-memory fallback.")
    mongo_client = None
    mongo_db = None
    users_collection = None
    mbti_collection = None
    quiz_sessions_collection = None

# === Redis Setup ===
try:
    redis_client = redis.from_url(REDIS_URL, socket_connect_timeout=3)
    redis_client.ping()
    print("[Redis] Connected successfully.")
except redis.exceptions.ConnectionError as e:
    print("[Redis] Connection failed. Using mock Redis.")
    class MockRedis:
        def __init__(self):
            self.store = {}
        def setex(self, key, ttl, value):
            self.store[key] = value
        def get(self, key):
            return self.store.get(key)
    redis_client = MockRedis()
