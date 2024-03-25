import uvicorn

# TODO Uncomment when need some tables and fake data
# import asyncio
# from populate import create_tables
# from src.graphql.db.session import engine

from src.graphql.core.config import settings
from src.app import create_app

application = create_app()

if __name__ == "__main__":
    print("Populating database...")
    # asyncio.run(create_tables(engine)) # use if need data uncomment this
    print("Database populated.")
    print("Starting server...")
    uvicorn.run("main:application", host=settings.HOST_URL, port=settings.HOST_PORT, reload=True)
