# Genesis Tech Task

How to run

```sh
# Allocate env
$ python3 -m venv env/

# Active env
$ source env/bin/activate

# Requirements
$ pip install -r requirements.txt

# Build docker images and start containers
$ docker-compose build; docker-compose up
```

For testing


```sh
# Run mongo container
$ docker-compose up mongo

# Run tests with pytest
$ pytest
```
