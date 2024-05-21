from fastapi import FastAPI
import router
import asyncio

app = FastAPI()

#define endpoint
@app.get("/")
def home():
    return "Welcome Home"

app.include_router(router.route)
asyncio.create_task(router.consume())
