REGISTRY_URL=australia-southeast1-docker.pkg.dev/beacon-guardians/beacon-images

	
docker:
	docker buildx build --platform linux/amd64 -t ${REGISTRY_URL}/beacon-app:v1 . --push
