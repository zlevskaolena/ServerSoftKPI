# ServerSoftKPI

This is a backend application for the ServerSoftKPI project. It is a web service built using Flask and Docker.

## Prerequisites

To run this project, you need:

- Docker
- Docker Compose


### Build and Run with Docker Compose

Run the following command to build the Docker image and start the containers:

```bash
docker-compose up --build
```

This will start the Flask web service on port 5000.

### Verify the Service

Once the containers are up and running, you can verify the service by visiting:

- **Localhost URL:**  
  `http://localhost:5000`
  
- **Docker Container URL (inside the container):**  
  `http://172.18.0.2:5000`

If everything is set up correctly, the service should respond to requests.

### Stopping the Containers

To stop the containers, press `CTRL + C` in the terminal or run:

```bash
docker-compose down
```

## Troubleshooting

If you encounter any issues, check the Docker logs for errors or issues with the Flask application:

```bash
docker logs container_name
```
