from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

VERSION = "v3"

# Prometheus metrics
metrics = PrometheusMetrics(app)

@app.route("/")
def home():
    return f"""
    <h1>Progressive Delivery Demo</h1>
    <p>Application Version: {VERSION}</p>
    """

@app.route("/health")
def health():
    return {
        "status": "healthy",
        "version": VERSION
    }

@app.route("/version")
def version():
    return {
        "version": VERSION
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
