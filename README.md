# FastAPI with Graphql

### If you want use this project like template git clone it and use it

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
