# Python  REST API assignment

A small REST API without authentication. Built with Django Rest Framework. Can be used to create, read, update and delete posts and users. When <id> of a post is not found in local database, it will be retrieved from the remote API.
## Installation Instructions:

- Git clone the repository and make a new virtual enviroment.

```
python -m venv <yourenviromentname>
```

- Activate the virtual enviroment by running the following command:

```
source <path-to-your-enviroment-name>/bin/activate
```

- Install the dependencies by running the following command:

```
pip install -r requirements.txt
```

- From project top level path, run this command to create a local SQLite file:


```
python manage.py migrate
```

- Run the local Django server by the following command:


```
python manage.py runserver
```

A local server will be started on port 8000. To change the port settings use the following command:

```
python manage.py runserver 0.0.0.0:<your_port>
```

- Note: When running on some linux distributions you may need to use the following command:

```
python3 manage.py runserver
```

## Basic Usage

When local server is running you can use the following URL to read the API documentation and HTTP methods:
-(note: change the port number in the URL path to your local server you specified in ```python manage.py runserver``` command )



```
http://127.0.0.1:8000/
```

Posts endpoints can be used to create, read, update and delete data via browsable API view.

```
http://127.0.0.1:8000/amcefapi/posts/
```

Users endpoint can be used to access list of users and create new users via browsable API view.

```
http://127.0.0.1:8000/amcefapi/users/
```

## Docker

Docker configuration file included in the repository. This repository is configured to run with local SQLite file. To run the docker container you need to run the following command:

```
docker-compose up -d
```


















```
