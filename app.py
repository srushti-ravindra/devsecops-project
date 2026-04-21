from flask import Flask, request

app = Flask(__name__)

# Vulnerable login (intentionally bad for demo)
@app.route('/login', methods=['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    # ❌ Hardcoded credentials (security issue)
    if username == "admin" and password == "admin123":
        return "Login Successful"
    else:
        return "Login Failed"

@app.route('/')
def home():
    return "Welcome to DevSecOps App"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)