from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

from models.schemas import Rental
from utils.auth_utils import verify_token

rentals_router = APIRouter()

fake_rental_db = [] 

@rentals_router.post("/rentals", response_class=JSONResponse)
async def rent_movie(rental: Rental, token: str = Depends(verify_token)):
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")

    fake_rental_db.append(rental)
    return JSONResponse(
        content={"msg": "Rental", "Owner": rental.user.username },
        status_code=201
    )


@rentals_router.get("/rentals", response_model=List[Rental])
async def get_rentals(token: str = Depends(verify_token)):
   if not token:
       raise HTTPException(status_code=401, detail="Not authenticated")
   current_user = token["sub"]
   user_rentals = [rental for rental in fake_rental_db if rental.user.username == current_user]
   return user_rentals

