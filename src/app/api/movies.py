from typing import List

from app.api import crud_movies
from app.api.models import MovieDB, MovieSchema
from fastapi import APIRouter, HTTPException, Path

router = APIRouter()


@router.post("/", response_model=MovieDB, status_code=201)
async def create_movie(payload: MovieSchema):
    movie_id = await crud_movies.post(payload)

    response_object = {
        "id": movie_id,
        "release_year": payload.release_year,
        "title": payload.title,
        "origin_ethnicity": payload.origin_ethnicity,
        "director": payload.director,
        "cast": payload.cast,
        "genre": payload.genre,
        "wiki_page": payload.wiki_page,
        "plot": payload.plot
    }
    return response_object


@router.get("/{id}/", response_model=MovieDB)
async def read_movie(id: int = Path(..., gt=0), ):
    movie = await crud_movies.get(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie


@router.get("/release_year/{year}/", response_model=List[MovieDB])
async def read_movie_release_year(year: str = Path(...), ):
    print(type(year))
    movie = await crud_movies.get_release_year(year)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie


@router.get("/", response_model=List[MovieDB])
async def read_all_movies():
    return await crud_movies.get_all()


@router.put("/{id}/", response_model=MovieDB)
async def update_movie(payload: MovieSchema, id: int = Path(..., gt=0), ):
    movie = await crud_movies.get(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    movie_id = await crud_movies.put(id, payload)

    response_object = {
        "id": movie_id,
        "release_year": payload.release_year,
        "title": payload.title,
        "origin_ethnicity": payload.origin_ethnicity,
        "director": payload.director,
        "cast": payload.cast,
        "genre": payload.genre,
        "wiki_page": payload.wiki_page,
        "plot": payload.plot
    }
    return response_object


@router.delete("/{id}/", response_model=MovieDB)
async def delete_movie(id: int = Path(..., gt=0)):
    movie = await crud_movies.get(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    await crud_movies.delete(id)

    return movie
