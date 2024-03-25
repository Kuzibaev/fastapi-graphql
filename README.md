# FastAPI with Graphql

### If you want use this project like template git clone it and use it

#### Edit envs folder's env files if you are in prod just use .env either .env.dev or .env.test

#### here example

```Bash
HOST_URL=
HOST_PORT=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_SERVER=
POSTGRES_PORT=
POSTGRES_DB=
```

### Installation

#### create virtualenv

```Bash
python -m venv venv
source venv/bin/activate
```

### Install requirements.txt

```Bash
pip install -r requirements.txt
```

### Running project

#### Prod

```Bash
python main.py 
```

#### Dev

```Bash
python main_dev.py 
```

### Migrations

```Bash
alembic revision --autogenerate -m "migration string"
alembic upgrade head
```
