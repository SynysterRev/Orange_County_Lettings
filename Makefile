include .env
export

build:
	docker build --build-arg SECRET_KEY="$$(SECRET_KEY)" -t ${user}/orange-county-lettings:latest .
	
push:
	docker push ${user}/orange-county-lettings
	
run: 
	docker run --env-file .env -p 8000:8000 ${user}/orange-county-lettings:latest
	
full: build push run