from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry.schema.config import StrawberryConfig
from src.graphql.schemas.mutation_schema import Mutation
from src.graphql.schemas.query_schema import Query

schema = strawberry.Schema(query=Query, mutation=Mutation, config=StrawberryConfig(auto_camel_case=True))


def create_app():
    app = FastAPI()
    create_create_middlewares(app)
    graphql_app = GraphQLRouter(schema)
    app.include_router(graphql_app, prefix="/graphql")
    return app


def create_create_middlewares(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Update this to allow specific origins
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
