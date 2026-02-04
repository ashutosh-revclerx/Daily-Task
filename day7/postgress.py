"""
Day 7: PostgreSQL Implementation (Docker-based)
Driver: psycopg v3
Covers:
- DB connection
- Schema creation
- Sample data insertion
- Complex queries (JOIN, LEFT JOIN, Subquery, CTE)
- Index creation
- EXPLAIN ANALYZE
"""

import psycopg


# =========================
# Database Configuration
# =========================
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "app_db",
    "user": "app_user",
    "password": "strongpassword",
}


def get_connection():
    conn = psycopg.connect(**DB_CONFIG)
    conn.autocommit = True
    return conn


# =========================
# Schema Creation
# =========================
def create_tables(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(150) UNIQUE NOT NULL
            );

            CREATE TABLE IF NOT EXISTS orders (
                id SERIAL PRIMARY KEY,
                user_id INT REFERENCES users(id),
                amount NUMERIC(10,2),
                created_at TIMESTAMP DEFAULT NOW()
            );

            CREATE TABLE IF NOT EXISTS payments (
                id SERIAL PRIMARY KEY,
                order_id INT REFERENCES orders(id),
                status VARCHAR(50)
            );
        """)
    print("✅ Tables created")


# =========================
# Seed Data
# =========================
def seed_data(conn):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id",
            ("Alice", "alice@example.com")
        )
        alice_id = cur.fetchone()[0]

        cur.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id",
            ("Bob", "bob@example.com")
        )
        bob_id = cur.fetchone()[0]

        cur.execute(
            "INSERT INTO orders (user_id, amount) VALUES (%s, %s) RETURNING id",
            (alice_id, 600)
        )
        order_id = cur.fetchone()[0]

        cur.execute(
            "INSERT INTO orders (user_id, amount) VALUES (%s, %s)",
            (alice_id, 200)
        )

        cur.execute(
            "INSERT INTO payments (order_id, status) VALUES (%s, %s)",
            (order_id, "SUCCESS")
        )

    print("✅ Sample data inserted")


# =========================
# Complex Queries
# =========================
def run_queries(conn):
    with conn.cursor() as cur:

        print("\n--- INNER JOIN ---")
        cur.execute("""
            SELECT u.name, o.amount
            FROM users u
            JOIN orders o ON u.id = o.user_id
        """)
        print(cur.fetchall())

        print("\n--- LEFT JOIN (users without orders) ---")
        cur.execute("""
            SELECT u.name
            FROM users u
            LEFT JOIN orders o ON u.id = o.user_id
            WHERE o.id IS NULL
        """)
        print(cur.fetchall())

        print("\n--- SUBQUERY ---")
        cur.execute("""
            SELECT name
            FROM users
            WHERE id IN (
                SELECT user_id FROM orders WHERE amount > 500
            )
        """)
        print(cur.fetchall())

        print("\n--- CTE (Total Spend per User) ---")
        cur.execute("""
            WITH total_spend AS (
                SELECT user_id, SUM(amount) AS total
                FROM orders
                GROUP BY user_id
            )
            SELECT u.name, t.total
            FROM total_spend t
            JOIN users u ON u.id = t.user_id
        """)
        print(cur.fetchall())

        print("\n--- MULTI TABLE JOIN ---")
        cur.execute("""
            SELECT u.name, o.id, p.status
            FROM users u
            JOIN orders o ON u.id = o.user_id
            JOIN payments p ON o.id = p.order_id
        """)
        print(cur.fetchall())


# =========================
# Index + EXPLAIN ANALYZE
# =========================
def optimize_queries(conn):
    with conn.cursor() as cur:
        cur.execute(
            "CREATE INDEX IF NOT EXISTS idx_orders_user_id ON orders(user_id);"
        )

        print("\n--- EXPLAIN ANALYZE ---")
        cur.execute(
            "EXPLAIN ANALYZE SELECT * FROM orders WHERE user_id = 1;"
        )
        for row in cur.fetchall():
            print(row[0])


# =========================
# Main Execution
# =========================
def main():
    conn = get_connection()

    create_tables(conn)
    seed_data(conn)
    run_queries(conn)
    optimize_queries(conn)

    conn.close()
    print("\n🎯 Day 7 PostgreSQL tasks completed successfully")


if __name__ == "__main__":
    main()
