"""Main server file for FastAPI application."""
import os
import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
from project_name.routers import info, fakedata

load_dotenv()

app = FastAPI()
app.include_router(info.router, prefix="/info", tags=["Info"])
app.include_router(fakedata.router, prefix="/fakedata", tags=["Fake Data"])

@app.get('/PING')
def ping() -> str:
    """Return tesing PONG"""
    return 'PONG'

if __name__ == "__main__":
    uvicorn.run(
        app,
        host='0.0.0.0',
        port=int(os.getenv("SERVER_PORT",'3030'))
    )
