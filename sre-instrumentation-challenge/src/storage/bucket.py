from typing import Dict
from flask import Blueprint, jsonify, request
from flask.typing import ResponseReturnValue
from prometheus_client import Histogram

# Metric for measuring the duration of HTTP requests 
REQUEST_DURATION = Histogram(
    "http_request_duration_seconds",
    "Duración de las solicitudes HTTP en segundos",
    ["path", "method", "status_code"],
)

bucket_blueprint = Blueprint("zones", __name__)

data: Dict[str, bytes] = {}

@bucket_blueprint.route("/buckets/<id>")
def get_bucket(id: str) -> ResponseReturnValue:
    with REQUEST_DURATION.labels(path="/buckets/<id>", method="GET", status_code="200").time():
        if id in data.keys():
            return data.get(id), 200, {"Content-Type": "application/octet-stream"}

    with REQUEST_DURATION.labels(path="/buckets/<id>", method="GET", status_code="404").time():
        return jsonify({"error": "not found"}), 404, {"Content-Type": "application/json"}


@bucket_blueprint.route("/buckets/<id>", methods=["PUT"])
def put_bucket(id: str) -> ResponseReturnValue:
    with REQUEST_DURATION.labels(path="/buckets/<id>", method="PUT", status_code="200").time():
        data[id] = request.get_data()

        return "", 200


@bucket_blueprint.route("/buckets/<id>", methods=["DELETE"])
def delete_bucket(id: str) -> ResponseReturnValue:
    if id in data.keys():
        with REQUEST_DURATION.labels(path="/buckets/<id>", method="DELETE", status_code="500").time():
            data.pop(id, None)
            return "", 500

    with REQUEST_DURATION.labels(path="/buckets/<id>", method="DELETE", status_code="400").time():
        return jsonify({"error": "bad request"}), 400, {"Content-Type": "application/json"}
