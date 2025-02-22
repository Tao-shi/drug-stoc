# Jenkins Pipeline for Flask App Deployment

This pipeline automates the build, test, and deployment of a simple Flask app. It includes stages for workspace cleanup, environment setup, linting, unit testing, Docker image creation, pushing the image to Docker Hub, and deploying to Kubernetes.

 

## Pipeline Stages

1. Clean Workspace: Cleans the Jenkins workspace.
2. Checkout: Clones the GitHub repository.
3. Env Setup: Sets up a Python virtual environment and installs dependencies.
4. Lint: Runs flake8 for code linting.
5. Unit Tests: Executes unit tests using pytest.
6. Build Docker Image: Builds a Docker image for the app.
7. Push Docker Image: Pushes the Docker image to Docker Hub.
8. Deploy to Kubernetes: Updates the Kubernetes deployment with the new image.



## Prerequisites

Before running the pipeline, ensure the following:

### Jenkins:

Installed with the following plugins:

- Pipeline
- Docker Pipeline
- Kubernetes CLI
- Workspace Cleanup Plugin

### Docker:

- Docker installed on the Jenkins server.
- Docker Hub credentials (DOCKER_USER and DOCKER_TOKEN) stored in Jenkins.

### Kubernetes:

- kubectl configured on the Jenkins server.
- A deployment named nginx exists in the cluster.

### GitHub Repository:

- Contains the following files:
- requirements.txt
- Dockerfile
- Unit tests in the tests/ directory.



## How to Use

1. Set Up Jenkins:
- Create a new pipeline job.
- Configure the pipeline to use the Jenkinsfile from your GitHub repository. 

2. Run the Pipeline:
- Trigger the pipeline manually or via GitHub webhooks.

3.  Monitor Progress:
- Check the Jenkins UI for pipeline status and logs.



## Customization

### Docker Image:
- Update the DOCKER_IMAGE environment variable to match your Docker Hub repository.

### Kubernetes Deployment:
- Update the DEPLOYMENT_NAME and CONTAINER_NAME variables to match your Kubernetes deployment.

### GitHub Repository:
- Update the REPO_URL variable to point to your GitHub repository.