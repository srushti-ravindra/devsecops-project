# ❌ Hardcoded secret (Security issue)
password = "admin123"

# ❌ Weak hashing (bad practice)
import hashlib
hashed = hashlib.md5(password.encode()).hexdigest()

# ❌ SQL Injection example
import sqlite3
conn = sqlite3.connect("test.db")

user_input = input("Enter username: ")
query = "SELECT * FROM users WHERE name = '" + user_input + "'"
conn.execute(query)

# ❌ Code smell: deep nesting
def calc(a, b):
    if a == 1:
        if b == 2:
            if a + b == 3:
                print("Nested logic")

# ❌ Debug leftover
print("DEBUG MODE ON")

# ❌ Unused variable (code smell)
temp = 12345