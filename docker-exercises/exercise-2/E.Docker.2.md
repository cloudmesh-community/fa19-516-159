# E.Docker.2: MongoDB Container with Authentication

## Steps

1) Build the image

	* docker build -t mongoimage .

2) Create a container based of "mongoimage" named "mongoContainer"

	* docker run -it --name mongoContainer -d mongoimage

3) Check the IP Address of mongoContainer

	* docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mongoContainer

4) Create another container (named mongoClient) and run bash shell. Note that this is runnning on Windows

	* winpty docker run -it -link=mongoContainer:mongoimage --name mongoClient mongoimage bash

5) Connect to mongoDB server from the client container shell, using IP from step 3 and standard port

	* mongo 172.17.0.2:27017

6) Create a user in the demo database

	* use demo
	* db.createUser({user:'testUser', pwd:'testpass', roles:[{role: 'read', db:'demo'}]})
