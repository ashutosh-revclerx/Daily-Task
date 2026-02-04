import redis
import json

# to run docker compose -f docker compose.redis.yml up -d
# Redis running in Docker (localhost exposed)
r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

def get_user(user_id):
    key = f"user:{user_id}"

    cached = r.get(key)
    if cached:
        print("✅ REDIS HIT")
        return json.loads(cached)

    print("❌ REDIS MISS → DB")
    user = {"id": user_id, "name": "Ashu"}

    r.setex(key, 300, json.dumps(user))
    return user

if __name__ == "__main__":
    print(get_user(1))
    print(get_user(1))
