from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.get("/")
def index():
    return jsonify(
        {
            "service": "smartgenie-agent-assistant",
            "status": "running",
            "environment": os.getenv("APP_ENV", "dev"),
            "capability": "conversation-and-routing",
        }
    )


@app.get("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.get("/respond")
def respond():
    return jsonify(
        {
            "message": "Assistant agent is ready to respond.",
            "mode": os.getenv("APP_ENV", "dev"),
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
