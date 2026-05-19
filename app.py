import streamlit as st
import mysql.connector
import bcrypt
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database Connection
conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    port = int(os.getenv("DB_PORT").strip().replace(",", "")),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255)
  )
""")

conn.commit()

st.title("Login & Signup App")

menu = ["Login", "Signup"]
choice = st.sidebar.selectbox("Select Option", menu)

# ---------------- SIGNUP ----------------

if choice == "Signup":

    st.subheader("Create New Account")

    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Signup"):  
         # Password Hashing
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Insert User
        query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"

        values = (
            username,
            email,
            hashed_password.decode('utf-8')
        )

        cursor.execute(query, values)
        conn.commit()

        st.success("Account Created Successfully")

# ---------------- LOGIN ----------------

elif choice == "Login":
    st.subheader("Login Account")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        query = "SELECT * FROM users WHERE email = %s"

        cursor.execute(query, (email,))

        user = cursor.fetchone()

        if user:

            stored_password = user[3]

            if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                st.success(f"Welcome {user[1]}")
            else:
                st.error("Incorrect Password")

        else:
            st.error("User Not Found")
