
## [Unreleased] - 2024-11-24

### Testing
- Change order for GET call in scripts/generate_traffic.sh, so now the 404 error codes are more commons.
- Added into scripts/README.md a different way to obtain 404 error codes

### Added
- Included a README.md file in ´kubernetes/´ folder for details about the configuration 
- Basic kubernetes configuration for prometheus + grafana + storage-api in folder ´kubernetes/´
- Added the dashboard for the challenge in dashboard/axpo-grafana.json and included into docker-compose.yml
- docker-compose.yml section for storage-api
- Dockerfile for storage-api solution
- Added ´http_request_duration_seconds´ metric for the three following methods:
  - `GET /buckets/<id>`
  - `PUT /buckets/<id>`
  - `DELETE /buckets/<id>`
- Included ´/metrics´ endpoint of the blueprint in ´src/storage/__init__.py´
- Added prometheus librarie for python ´prometheus_client>=0.21.0´ in setup.py