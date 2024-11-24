from flask import Flask, Response

from storage.bucket import bucket_blueprint
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__, static_url_path="", static_folder="../static")
app.config.from_object(__name__)
app.register_blueprint(bucket_blueprint, url_prefix="/api")

# Endpoint '/metrics' out of the blueprint above.
@app.route("/metrics")
def metrics() -> Response:
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)