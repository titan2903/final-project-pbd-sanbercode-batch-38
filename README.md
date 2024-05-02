# Final Project - Titanio Yudista - PBD Sanbercode Batch 38

## Setup Project

1. Create database in **PostgreSQL** for the project, because I used **PostgreSQL** for Database in this Project.
2. Create table for the project, example for create table in here [**Example create table**](https://gitlab.com/titan03/final-project-titanio-yudista-pbd-sanbercode-batch-38/-/blob/main/create_table_example.sql).
3. Clone this **repository**:

    ```bash
    With SSH: 
    git@gitlab.com:titan03/final-project-titanio-yudista-pbd-sanbercode-batch-38.git

    With URL:
    https://gitlab.com/titan03/final-project-titanio-yudista-pbd-sanbercode-batch-38.git
    ```

4. Go to  directory `final-project-titanio-yudista-pbd-sanbercode-batch-38` with this command line, if the folder in your path **home**:

    ```shell
    cd ~/final-project-titanio-yudista-pbd-sanbercode-batch-38
    ```

5. Import data **products.csv** and **users.csv** to table **users** and **products**, you can find the data in here [**Data Products**](https://gitlab.com/titan03/final-project-titanio-yudista-pbd-sanbercode-batch-38/-/blob/main/products.csv) and [**Data Users**](https://gitlab.com/titan03/final-project-titanio-yudista-pbd-sanbercode-batch-38/-/blob/main/users.csv), and then download the **CSV** file, to be imported into the **table** that has been created.
6. Add `.env` file with this command in your terminal VS Code:

    ```shell
    cp .env.example .env 
    ```

7. After running command line `cp .env.example .env`, you have to **setup** some environment variables you need in the **.env** file. For the example **environtment variables setup**:

   ```bash
    DATABASE_CONN="postgresql://dbusername:dbpassword@localhost/dbname"
    JWT_SECRET="s3cr3t"
    JWT_ALGORITHM="HS256"
   ```

## Installation dependency

1. Install `fasapi` framework

    ```bash
    pip install fastapi
    ```

2. Install `uvicorn` to work as the server

    ```bash
    pip install "uvicorn[standard]"
    ```

3. Install the `python-decouple` module in your Python environment

    ```bash
    pip install python-decouple
    ```

4. Install `sqlalchemy` is a popular SQL toolkit and Object-Relational Mapping (ORM) library for Python

    ```bash
    pip install sqlalchemy
    ```

5. Install : Instead of installing `psycopg2`, you can install `psycopg2-binary`, which is a pre-built binary package and does not require compilation

    ```bash
    pip install psycopg2-binary
    ```

6. Install PostgreSQL development files

   ```bash
   sudo apt update && sudo apt-get install libpq-dev -y
   ```

7. Install `psycopg2`, which is a PostgreSQL adapter for Python

    ```bash
    pip install psycopg2
    ```

8. Install `passlib` module, which is a Python library for hashing passwords

   ```bash
   pip install passlib

   ```

## Running the Server

1. Open terminal in your VS Code.
2. Put this command line in Terminal VS Code:

    ```shell
    uvicorn main:app --reload
    ```

3. Server will be running in this [**localhost**](http://127.0.0.1:8000/products).

## Swagger Documentation

- **After Server Running** you can view the **Documentation** via **Swagger** here [**Swagger Documentation**](http://127.0.0.1:8000/docs).

## Postman Collection

- If you want hit API with **Postman**, you can import this [**Postman Collection**](https://gitlab.com/titan03/final-project-titanio-yudista-pbd-sanbercode-batch-38/-/blob/main/final%20project.postman_collection.json).
  
## About this Final Project

This is a simple CRUD project. There are three tables for storing the input data, namely the Products table (to store data products), the Users table (to store Users data) and the Contacts table (to store the contacts of registered users). In this project I use several stacks such as:

- **PostgreSQL** as a Database to store the data input by the user or admin,
- **FastAPI** as a framework to create RESTful API in this project,
- **Python** is the programming language that I use to create a RESTful API in this project,
- And use **JWT** for `Authentication` and `Authorization` when the user login into the application.

## Entity Relationship Diagram (ERD)

- Database design for this project. [**Click this for Entity Relationship Diagram**](https://dbdiagram.io/d/63411138f0018a1c5fbe24ac)

## Server Deployed on Heroku

- Health check successfully deployed [**Health Check Endpoint**](https://pacific-dusk-20067.herokuapp.com/)
