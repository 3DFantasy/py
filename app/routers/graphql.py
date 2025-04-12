from fastapi import APIRouter, Request
from strawberry.fastapi import GraphQLRouter
from app.schemas.schema import schema

router = APIRouter()


# Define a context getter function that includes the request
async def get_context(request: Request):
    return {"request": request}


graphql_app = GraphQLRouter(schema, context_getter=get_context)

router.include_router(graphql_app, prefix="/graphql")
