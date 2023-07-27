# prediction-web-app
A web application for predicting chemical properties relevant to combustion. Built using Python, Django, PostgreSQL, PyTorch, and RDKit.

Set the following environment variables (or create a `.env` file):

```
POSTGRES_DB=prediction-app-db
POSTGRES_USER=prediction-app-user
POSTGRES_PASSWORD=prediction-app-password
POSTGRES_PORT=5432
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=example@example.com
DJANGO_SUPERUSER_PASSWORD=adminpassword
WEB_PORT=8000
```

Run with:

```
$ docker compose up -d
```
