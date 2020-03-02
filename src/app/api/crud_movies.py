from app.api.models import MovieSchema
from app.db import movies, database


async def post(payload: MovieSchema):
    query = movies.insert().values(
        release_year=payload.release_year,
        title=payload.title,
        origin_ethnicity=payload.origin_ethnicity,
        director=payload.director,
        cast=payload.cast,
        genre=payload.genre,
        wiki_page=payload.wiki_page,
        plot=payload.plot
    )
    return await database.execute(query=query)


async def get(id: int):
    query = movies.select().where(id == movies.c.id)
    return await database.fetch_one(query=query)

async def get_release_year(release_year: str):
    query = movies.select().where(release_year == movies.c.release_year)
    return await database.fetch_all(query=query)

async def get_all():
    query = movies.select()
    return await database.fetch_all(query=query)


async def put(id: int, payload: MovieSchema):
    query = (
        movies
            .update()
            .where(id == movies.c.id)
            .values(
                release_year=payload.release_year,
                title=payload.title,
                origin_ethnicity=payload.origin_ethnicity,
                director=payload.director,
                cast=payload.cast,
                genre=payload.genre,
                wiki_page=payload.wiki_page,
                plot=payload.plot
            )
            .returning(movies.c.id)
    )
    return await database.execute(query=query)


async def delete(id: int):
    query = movies.delete().where(id == movies.c.id)
    return await database.execute(query=query)
