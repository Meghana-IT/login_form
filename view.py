import mysql.connector

conn = mysql.connector.connect(
     host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT").strip().replace(",", "")),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM users")
data = cursor.fetchall()

for row in data:
    print(row)