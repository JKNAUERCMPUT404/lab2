#!/bin/bash
# Question 1
# python3 -u client.py

# For client/server interactions, launch the server in the container and then connect to the container
# using docker exec -it bash, and run the client connections from the shell

# Question 2
# python3 -u echo_server.py

# Proxy server and client
exec python3 -u proxy_server.py &
exec python3 -u proxy_client.py

