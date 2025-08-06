# Final Project – Flask Voting App with Docker and CI/CD

You are provided with a basic Python Flask application (`app.py`) that allows users to vote between "Cats" and "Dogs". Votes are stored in a Redis cache.

  

Your task is to:

  

1. Create a Dockerfile to containerize the application.

2. Create a compose.yaml file to run the application with Redis.

3. Create a GitHub Actions workflow to build and push the image to Docker Hub.

  

## Provided Files

  

You are given:

  

-  `app.py`: the Flask application code.

-  `requirements.txt`: the application dependencies.

  

You should not modify the provided code.

  

## Project Steps

  
  
  

### Step 1: Create a Dockerfile

  

- Use the official Python image (e.g., python:3.10-slim).

- Set the working directory.

- Copy `requirements.txt` and install dependencies.

- Copy the application files.

- Use `flask run` to start the server.

- Make sure the app listens on `0.0.0.0` .

  
  
  

### Step 2: Create a compose.yaml file

  

The file must define two services:

  

1.  `web`:

- Builds the image using your Dockerfile.

- Exposes port 5000.

- Depends on the Redis service.

2. `redis`:

- Uses the official `redis` image.
  

### Step 3: Create a GitHub Actions workflow

  

The workflow must do the following:

 - Trigger on pull request and push to the `main` branch.
 
 - Checkout the code

 - Log in to Docker Hub using repository secrets and vars:

    - `DOCKER_USERNAME`
   
    -  `DOCKER_PASSWORD`

 - Build the Docker image and tag it with the current commit SHA.

 - Push to Docker Hub.

-----

#### Bonus:

- Tag the image with a second tag `latest`

- Push both tags to Docker Hub.

  
####  Final Checklist

-   Dockerfile is correctly implemented.
    
-   compose.yaml runs the app with Redis.
    
-   GitHub Actions workflow builds and pushes the image automatically.
    
-   Image has SHA tag (and optionally latest tag).
    
  

### Submission

After completing all the steps:

1.  Make sure all your changes are pushed to your GitHub repository.
    
2.  Copy the URL of your repository.
    
3.  Go to the following link: [Project Submission Link](https://github.com/faialotaibi/DevOps-Course/issues/7)
    
4.  Comment with the following:
        
    -   Write you full name.
        
    -   Paste the link of your project solution repository.