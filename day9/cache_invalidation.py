import redis

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

def update_user(user_id, new_name):
    print("📝 Updating DB (simulated)")
    print(f"🧹 Deleting cache for user:{user_id}")

    r.delete(f"user:{user_id}")

if __name__ == "__main__":
    update_user(1, "NewName")
