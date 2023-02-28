# semantics
Created for L3T12

## Purpose
This project was created as part of a task for the Hyperiondev Software Engineer bootcamp. 
The focus of this task is to use the spaCy module to detect semantic similarity in text.

## Requriements
1. Python 3 (https://www.python.org/downloads/)
2. pip (https://pip.pypa.io/en/stable/installation/)

## Installation
1. Clone the repository to a directory on your computer.
2. In command line navigate to the directory and run 'pip install -r requirements.txt'

## Usage
This script will print out the following in this order:
1. The similarity between the following words
   1. cat & monkey
   2. banana & monkey
   3. banana & cat
   
2. A list of the similarity ratings between the words cat, monkey, banana & apple

3. A comparison of the similarity of the sentence "Why is my cat on the car" to five other sentences

You can run the script either through an IDE of your choice or in command prompt using the command 'python semantic.py' in the root directory of the project. 
I have also provider a Dockerfile so you can creat an image of the project and run it in a container using Docker.
The output should look like this:

![semantic](https://user-images.githubusercontent.com/15369629/221988355-7f49e732-0a0a-401c-aa7a-33d31d23665d.png)

## Running in a container
To run this project in a container you will either need to install Docker Decktop (https://www.docker.com/) or creat an account on Docker and use Docker Playground (https://labs.play-with-docker.com/)

### To run with Docker Desktop
1. Using command line in the root directory for the project (where the Dockerfile is found) run 
   'docker build -t [Enter a tag for the image] ./'
2. Once this has finished you can now run the script using
   'docker run [the tag you chose]'

### To run in docker playground
1. Follow step 1 from the Docker Desktop instructions to build the image.
2. In command line enter 'docker login' and enter your login details for docker hub.
3. On docker hub you will need to create a repository and then retag the local image to match your repository's name.
   to do this in command line run
   'docker tag [local tag for the image] [user]/[repo]'
   where user is your Docker hub username and repo is the repositories name.
4. Now upload the image by entering
   'docker push [user]/[repo]'
5. Now you can login to Docker playground with your Docker account and start a session and begin a new instance/
6. In the instance enter
   'docker run [user]/[repo]'

This should return a result similar to the example above.

## Credits
- Murray Bosworth
- https://www.hyperiondev.com/ for their course resources
