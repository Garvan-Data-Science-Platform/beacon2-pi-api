# Config for local deployment with minikube and helm
LOCAL_DEPLOYMENT:=beacon-local
LOCAL_CONFIG:=demoMode.enabled=true,$\
	userClient.image.repository=docker.io/library/user-client,$\
	userClient.image.pullPolicy=Never,$\
	adminClient.image.repository=docker.io/library/admin-client,$\
	adminClient.image.pullPolicy=Never,$\
	backend.image.repository=docker.io/library/backend,$\
	backend.image.pullPolicy=Never

# Local deployment via minikube and helm

# Build images

kube-start:
	minikube start

kube-delete:
	minikube delete

docker:
	eval $$(minikube -p minikube docker-env) && \
	docker compose -f ../docker-compose.no-idp.yml build 

config:
	kubectl create configmap mongo-init-cm --from-file=init-script.js=../beacon/connections/mongo/mongo-init/init.js
	kubectl create configmap beacon-config-cm --from-file=conf.py=../beacon/conf/conf.py
	kubectl create configmap beacon-permissions-cm --from-file=../beacon/permissions/

apply:
	kubectl apply -f $$(find . -maxdepth 1 -name "*.yaml" | paste -s -d ',' -)

install:
	helm install $(LOCAL_DEPLOYMENT) .helm/ctrl \
		--set $(LOCAL_CONFIG)

upgrade:
	helm upgrade $(LOCAL_DEPLOYMENT) .helm/ctrl \
		--set $(LOCAL_CONFIG)

uninstall:
	helm uninstall $(LOCAL_DEPLOYMENT)
