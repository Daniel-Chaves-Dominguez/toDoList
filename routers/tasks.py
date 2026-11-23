from fastapi import APIRouter, HTTPException

from models.Task import Task


router = APIRouter(
    prefix='/tasks',
    tags=['Tasks']
)

task_list = {}
counter = 1


@router.get('/')
def get_tasks():
    return list(task_list.values())

@router.post('/', status_code=201)
def create_task(task: Task):
    global counter
    task_list[counter] = task
    counter += 1
    return task

@router.get('/{id}')
def read_task(id: int):
    if task_list.get(id) == None:
        raise HTTPException(status_code=404, detail='The task does not exist')
    return task_list[id]

@router.put('/{id}', status_code=204)
def update_task(id: int, task: Task):
    if task_list.get(id) == None:
        raise HTTPException(status_code=404, detail='The task does not exist')
    task_list[id] = task

@router.delete('/{id}', status_code=204)
def delete_task(id: int):
    if task_list.get(id) == None:
        raise HTTPException(status_code=404, detail='The task does not exist')
    task_list.pop(id)
