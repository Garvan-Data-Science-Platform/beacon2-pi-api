# Local deployment via minikube

LOCAL_DEPLOYMENT:=beacon-local

.PHONY: kube-start help docker kube-vol config apply port-forward load-job delete-load-job \
	delete-all kube-delete help

kube-start: ## Start minikube cluster
	minikube start

docker: ## Build required docker images
	eval $$(minikube -p minikube docker-env) && \
	docker compose -f ../docker-compose.no-idp.yml build 

kube-vol: ## Create a minikube volume
	minikube ssh -- sudo mkdir -p /mnt/data/mongo

config: ## Create k8s configmaps
	kubectl create configmap mongo-init-cm --from-file=../beacon/connections/mongo/mongo-init/init.js
	kubectl create configmap beacon-config-cm --from-file=../beacon/conf/conf.py
	kubectl create configmap beacon-permissions-cm --from-file=../beacon/permissions/datasets/datasets_permissions.yml
	kubectl create configmap mongo-cohort-data-cm --from-file=../beacon/connections/mongo/data/rddp/cohorts.json

apply: ## Apply mongodb and beacon services
	kubectl apply -f mongodb.yaml
	kubectl apply -f beacon.yaml

port-forward: ## Port-forward to access api (for example: `make POD=beaconprod-6b46568b6b-6lfc9 port-forward`)
	kubectl port-forward $(POD) 5050:5050

delete-all: ## Delete all kubernetes resources
	kubectl delete -f .

install:
	helm install $(LOCAL_DEPLOYMENT) ./beacon

upgrade:
	helm upgrade $(LOCAL_DEPLOYMENT) ./beacon

uninstall:
	helm uninstall $(LOCAL_DEPLOYMENT)

load-job: ## Run data load job
	helm install cohort-data-load ./beacon-data-load
	#helm install data-load-$$(date +%Y%m%d%H%M%S) ./beacon-data-load/ -f config/local.yaml

#delete-load-job: ## Delete load job pod (logs will no longer be accessible)
#	kubectl delete -f load.yaml

kube-delete: ## Delete minikube cluster
	minikube delete

help: ## Display available commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk \
		'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
