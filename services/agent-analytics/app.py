from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.get("/")
def index():
    return jsonify(
        {
            "service": "smartgenie-agent-analytics",
            "status": "running",
            "environment": os.getenv("APP_ENV", "dev"),
            "capability": "analytics-and-insights",
        }
    )


@app.get("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.get("/metrics")
def metrics():
    return jsonify(
        {
            "eventsProcessed": 128,
            "insightsGenerated": 12,
            "queueDepth": 3,
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)  # nosec B104 - required for container ingress exposure
