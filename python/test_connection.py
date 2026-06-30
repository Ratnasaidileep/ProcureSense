import pymysql
from config import DB_CONFIG

try:
    connection = pymysql.connect(**DB_CONFIG)

    print("=" * 50)
    print("✅ Successfully connected to MySQL!")
    print("=" * 50)

    with connection.cursor() as cursor:
        cursor.execute("SELECT DATABASE();")
        db = cursor.fetchone()
        print(f"Current Database: {db[0]}")

    connection.close()

except Exception as e:
    print("❌ Connection Failed")
    print(e)