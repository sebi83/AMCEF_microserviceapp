# Python microservice REST API assignment

A small REST API microservice without authentication. Built with Django Rest Framework and viewsets. Can be used to create, read, update and delete posts and users, and to retrieve the posts of a specific user. When <id> is not found in local database it will be retrieved from the remote API in JSON format specified in userposts/views.py global URL\_<> variable and saved in local database.

## Installation Instructions:

- Git clone the repository and make a new virtual enviroment.

```
python -m venv <yourenviromentname>
```

- Activate the virtual enviroment by running the following command:

```
source <yourenviromentname>/bin/activate
```

- Install the dependencies by running the following command:

```
pip install -r requirements.txt
```

- From project top level path run the the local django server.

```
python manage.py runserver
```

A local server will be started on port 8000. To change the port settings run the following command:

```
python manage.py runserver 0.0.0.0:<your_port>
```

Note: When running on some linux distributions you may need use following command:

```
python3 manage.py runserver
```

## Basic Usage

When local server is running you can use the following url to read the API documentation and HTTP methods:

```
http://127.0.0.1:8000/amcefapi/
```

Posts endpoints can be used to create, read, update and delete data.

```
http://127.0.0.1:8000/amcefapi/posts/
```

Users endpoint can be used to access list of users and create new users.

```
http://127.0.0.1:8000/amcefapi/users/
```

## Docker

Docker configuration file included in the repository. This repository is configured to run with local sqlite file. To run the docker container you need to run the following command:

```
docker-compose up -d
```


















```
