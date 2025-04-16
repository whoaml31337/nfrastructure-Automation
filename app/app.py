from flask import Flask
from prometheus_client import generate_latest, Counter, Histogram

app = Flask(__name__)
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests')
REQUEST_TIME = Histogram('http_request_duration_seconds', 'HTTP Request Duration')

@app.route('/')
def hello():
    with REQUEST_TIME.time():
        REQUEST_COUNT.inc()
        return "Hello, World!"

@app.route('/metrics')
def metrics():
    return generate_latest()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)