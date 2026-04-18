# app.py

import os

def login(username, password):
    # ❌ Vulnerability: hardcoded credentials
    if username == "admin" and password == "admin123":
        return "Login Successful"
    else:
        return "Login Failed"

print(login("admin", "admin123"))