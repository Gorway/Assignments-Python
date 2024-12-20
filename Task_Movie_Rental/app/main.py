import os
from dotenv import load_dotenv


import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import auth_rout, movies_rout, rent_rout
from middlewears import log_middlewear
load_dotenv()


HOST = os.getenv("HOST")
PORT = int(os.getenv("PORT"))
JWT_TOKEN = os.getenv("JWT_SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
TOKEN_EXPIRY = os.getenv("ACCESS_TOKEN_EXPIRED_MINUTES")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(log_middlewear.LogMiddleware)

app.include_router(auth_rout.auth_router)
app.include_router(movies_rout.movies_router)
app.include_router(rent_rout.rentals_router)


if __name__ == "__main__":
    uvicorn.run("main:app", port=PORT, host=HOST, reload=True)
