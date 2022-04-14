from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

app = FastAPI()


@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'blog pusblished list {limit}'}
    else:
        return {'data': f'blog list {limit}'}


@app.get('/blog/unpupished')
def unpublished():
    return "unpublished"


@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id):
    return {'data': {'1', '2'}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(request: Blog, db):
    return {'data': f'Blog is created with {request.title}'}
