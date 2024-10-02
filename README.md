# AllesGUT

**AllesGut** is a personal server-side frontend project built using Django, designed to provide a scalable and modular solution for various applications. The project implements multiple apps under a unified architecture, featuring an eCommerce app where users can buy and sell anything, along with additional functionalities like finding IP addresses and location tracking.

The project adopts DRY (Don't Repeat Yourself) code principles to ensure maintainability and efficiency. Leveraging Celery for load balancing, it efficiently manages asynchronous tasks, enhancing the app's performance under heavy workloads.

AllesGut also uses Django REST Framework (DRF) to build and maintain a robust API layer, facilitating easy integration and future enhancements. This project aims to offer a clean, scalable backend solution for managing various real-world functionalities under a single platform.


## Key Features

- **eCommerce App:** Buy, sell, and list items seamlessly.
- **Find My IP:** Fetches IP address and location details.
- **Load Balancing:** Utilizes Celery to handle task queues for performance optimization.
- **DRY Code Concept:** Promotes reusability and maintainable code.
- **RESTful API:** Built using Django REST Framework for scalable API management.


## Tech Stack
- **Django:** Server-side frontend framework.
- **Celery:** Load balancing and task queue handling.
- **Redis:** Broker for Celery tasks.
- **Django REST Framework:** API development and management.
- **PostgreSQL:** Database for structured data.



## Step 1: Clone this repo to your local machine.
* To clone the repo , navigate to your desired project directory in your terminal or command prompt and run the following command:
    ```bash
    git clone <repo>

#### Note: this project is under development below details are may not be accurate
####       feel free to sujest corrections and contribution.

##  Step 2: Install virtual environment.
* To install virtual environment , you can use pip, which is Python's package manager. You can install it by. 
    ```bash
        pip install virtualenv

* And  then create a virtual environment by.
    ```bash
        virtualenv <env_name>

* Replace <env_name> with the name of your virtual environment.

* Activate  the virtual environment by.
    For macOS /Linux:
    ```bash
        source <env_name>/bin/activate
    
* For windows.
    ```bash
        <env_name>\Scripts\activate

* You should see the name of your virtual environment printed in your command line.

##   Step 3: Install required packages.
* To install the packages which are used for this project by running.
    ```bash
        pip install -r requirements.txt
    
This will install all the packages listed in the requirements.txt file.

##  Step 4: Configure AWS Transcribe and OpenAI.
* You need to configure AWS Transcribe and OpenAI in the config.py file.
* For AWS Transcribe, you need to set the ```AWS_ACCESS_KEY_ID```, ```AWS_SECRET_ACCESS_KEY```, and ```AWS_REGION_NAME``` variables.
* For OpenAI, you need to set the ```OPENAI_API_KEY``` variable.
* You can find these values in your AWS and OpenAI dashboards.
* Make sure to replace the placeholders with your actual values.
* for better practice use ```.env```

##   Step 5: Run the application.
* To run the application, navigate to the project directory in your terminal or command prompt
    For production.
    ```bash
        python manage.py runserver 
    ```
    For development.
    ```bash
        python manage.py runserver 
    ```
    or 
    ```bash
        python manage.py runserver 
    ```

    * This will start the application and you can access it by visiting http://localhost:8000 in your web browser.
    * You can use the API endpoints to interact with the application.

##   Docker Setup
if you want to run the project in docker follow the below steps:
* download docker on your system , check this docs for installation [install docker](https://docs.docker.com/engine/install/)
* make sure that you  have `Dockerfile` and `docker-compose.yml` in your root folder with appropiate values.
* run the following command to build the docker image.
    ```bash
        docker compose build
* incase the docker is not started use below command and retry to build `docker compose build`
    ```bash
        dockerd
* run the following command to compose up container.
    ```bash
        docker compose up
* you can access the app by visiting http://localhost:8000 in your web browser.
* if you want open any container in new terminal use below command.
    For Linux
    ```bash
        docker exec -it  <container_id or container_name> bash
* for listing containers which are running on you system 
    ```bash 
        docker ps


## Step  6: Test the application.

To test the endpoints , you can use a tool like Postman ,cURL or swagger
    You can find the API documentation in the /docs endpoint of the application http://localhost:8000python manage.py runserver /docs.
    You can use the API endpoints to test the functionality of the application.


## Contribution.

Feel  free to contribute to this project by submitting pull requests or issues.

## License.
This project is licensed under the MIT License.

