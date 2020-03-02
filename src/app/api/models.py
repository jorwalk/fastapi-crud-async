from pydantic import BaseModel, Field



class MovieSchema(BaseModel):
    release_year: str = Field(..., min_length=4, max_length=4)
    title: str = Field(..., min_length=0, max_length=128)
    origin_ethnicity: str = Field(..., min_length=0, max_length=32)
    director: str = Field(..., min_length=0, max_length=256)
    cast: str = Field(..., min_length=0, max_length=256)
    genre: str = Field(..., min_length=0, max_length=128)
    wiki_page: str = Field(..., min_length=0, max_length=256)
    plot: str = Field(..., min_length=0)

class MovieDB(MovieSchema):
    id: int
