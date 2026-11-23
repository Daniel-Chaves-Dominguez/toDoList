from fastapi import FastAPI

from routers import tasks

app = FastAPI(
    title='To Do List',
    description='An API to manage things',
    version='0.1.1'
)

app.include_router(tasks.router)

@app.get('/')
def welcome():
    return {'message': 'Welcome to the best API ever'}
