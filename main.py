import strawberry
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter

from api.author import router as author_router
from config import logger
from model.ql_mutation import Mutation
from model.ql_query import Query

# from api.book import router as book_router


app = FastAPI(title="Backend", version="0.1", docs_url="/docs")

origins = [
    "http://localhost:8080",
    # 'https://frontend.com',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)


@app.on_event("startup")
async def startup_event():
    logger.debug("Server Starting Up...")


@app.get("/")
async def health():
    return {"ping": "pong"}


@app.on_event("shutdown")
async def shutdown_event():
    logger.debug("Server Shutting Down...")


app.include_router(graphql_app, prefix="/graphql")
app.include_router(author_router)
# app.include_router(book_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
