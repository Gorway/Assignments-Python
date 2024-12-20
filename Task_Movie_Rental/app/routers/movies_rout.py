from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

from models.schemas import Movie
from utils.auth_utils import verify_token

movies_router = APIRouter()

fake_movie_db = []


@movies_router.get("/movies", response_model=List[Movie])
async def get_movies():
    return fake_movie_db


@movies_router.post("/movies")
async def add_movie(movie: Movie, token: str = Depends(verify_token)) -> str:
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    current_user = token["sub"]
    fake_movie_db.append(movie)
    return JSONResponse(
        content={"msg": "Movie added successfully", "added_by": current_user},
        status_code=201
    )

@movies_router.get("/movies/filter", response_model=List[Movie])
async def filter_movies(
    genre: Optional[str] = None,
    min_rating: Optional[float] = None,
    max_rating: Optional[float] = None,
):
    filtered_movies = fake_movie_db
    if genre:
        filtered_movies = [
            movie for movie in filtered_movies if movie.genre.lower() == genre.lower()
        ]
    if min_rating is not None:
        filtered_movies = [
            movie for movie in filtered_movies if movie.rating >= min_rating
        ]
    if max_rating is not None:
        filtered_movies = [
            movie for movie in filtered_movies if movie.rating <= max_rating
        ]
    return filtered_movies
