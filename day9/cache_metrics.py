import redis
import json

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

hits = 0
misses = 0

def get_user(user_id):
    global hits, misses

    key = f"user:{user_id}"
    cached = r.get(key)

    if cached:
        hits += 1
        return json.loads(cached)

    misses += 1
    user = {"id": user_id, "name": "Ashu"}
    r.setex(key, 300, json.dumps(user))
    return user

if __name__ == "__main__":
    for _ in range(5):
        get_user(1)

    hit_rate = hits / (hits + misses)
    print(f"Hit Rate: {hit_rate:.2f}")
