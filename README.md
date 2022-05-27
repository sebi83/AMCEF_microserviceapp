# Python microservice REST API assignment 

A small REST API microservice without authentication that can be used to create, read, update and delete data for a user.
---

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
---
## API swagger documentation

Run the following URL when local server is running:

```http://127.0.0.1:8000/swagger/```


---

## Usage

When local server is running you can use the following url to create, read, update and delete data in JSON format:

```http://127.0.0.1:8000/amcefapi/```


## List of available endpoints:


Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`amcefapi` | GET | READ | Overview of the API in JSON format
`amcefapi/posts/:id` | GET | READ | Get a single post by id
`amcefapi/post-create/`| POST | CREATE | Create a new post
`amcefapi/post-update/:id` | PUT | UPDATE | Update a post
`amcefapi/post-delete/:id` | DELETE | DELETE | Delete a post





