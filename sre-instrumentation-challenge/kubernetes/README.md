
# Namespace

There is a file called namespace.yaml with the configuration for the namespace where all our solution would be deployed 

# PVC

The file pvc.yaml will create the Persistence Volume for the Prometheus and Grafana solutions.

# Prometheus

The file prometheus.yaml has all the components needed for its deploy. It also has a ConfigMap where we will put our defined dashboard.

It will read the target from the service as follow:

´´´
targets: ["storage-api.axpo.svc.cluster.local:5000"]
´´´

# Grafana

The file grafana.yaml has all the needed for running grafana. It has 2 ConfigMaps. One for the configuration of the dashboard and another one for the dashboard itself. 

# Storage-api

The file storage-api.yaml has evertyhing needed for deploying the solution into a kubernetes cluster. The ingress for it was defined in a different file called ingress.yaml.

# Ingress

The idea is to have a unique ingress, and give the corresponding service depending on the given URI:

https://axpo.com/grafana
https://axpo.com/prometheus
https://axpo.com/storage-api

Note: This might required some particular configuration for relative paths. Not tested.