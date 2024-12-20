from pydantic import BaseModel, Field, EmailStr

class Token(BaseModel):
    access_token: str
    token_type: str

class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6)
    email: EmailStr


class Movie(BaseModel):
    title: str = Field(..., max_length=50)
    genre: str = Field(..., max_length=50)
    rating: int = Field(..., ge=1, le=10)


class Rental(BaseModel):
    user: User
    movie: Movie
    rental_duration: str

