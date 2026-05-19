import mysql.connector

conn = mysql.connector.connect(
     host=os.getenv("DB_HOST"),
    port = int(os.getenv("DB_PORT").strip().replace(",", "")),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255)
)
""")

conn.commit()