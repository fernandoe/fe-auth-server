# Docker

## Compose

```bash
docker-compose build fe_auth
docker-compose run --rm fe_auth pip3 install -r /requirements/docker.txt
docker-compose run --rm fe_auth pip3 install -r /requirements/development.txt
docker-compose run --rm fe_auth python3 manage.py migrate
docker-compose run --rm fe_auth python3 manage.py createsuperuser --email=test@test.com
docker-compose run --name fe_auth --rm --service-ports fe_auth /bin/bash
```



## Running local

```bash
docker build --no-cache -t local/fe-auth .
docker build -t local/fe-auth .
docker run --rm -i -t local/fe-auth /bin/bash
```

