# Local deployment via minikube and helm

# Build images

kube-start:
	minikube start

kube-delete:
	minikube delete

docker:
	eval $$(minikube -p minikube docker-env) && \
	docker compose -f ../docker-compose.no-idp.yml build 

kube-vol:
	minikube ssh -- sudo mkdir -p /mnt/data/mongo

config:
	kubectl create configmap mongo-init-cm --from-file=init-script.js=../beacon/connections/mongo/mongo-init/init.js
	kubectl create configmap beacon-config-cm --from-file=conf.py=../beacon/conf/conf.py
	kubectl create configmap beacon-permissions-cm --from-file=../beacon/permissions/

k8s-apply:
	kubectl apply -f .

k8s-delete:
	kubectl delete -f .
