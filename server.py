from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import time

print("SERVER STARTING")

app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["5 per second"]
)

@app.route("/")
def home():
    time.sleep(0.05)
    return "Server alive"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001)