from fastapi import APIRouter, HTTPException

from models.Task import Task


router = APIRouter(
    prefix='/tasks',
    tags=['Tasks']
)

task_list = {}
counter = 1


@router.get('/')
def get_tasks(completed: bool | None = None, title: str |None = None):
    to_return = list(task_list.values())
    if completed != None:
        #filtered = []
        #for task in list(task_list.values()):
            #if task.completed == completed:
                #filtered.append(task)
        to_return = [task for task in to_return if task.completed == completed]
    if title != None:
        to_return = [task for task in to_return if title in task.title]
    return to_return

@router.post('/', status_code=201)
def create_task(task: Task):
    task_list[task.id] = task
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
    if task.id != id:
        raise HTTPException(status_code=400, detail='The ID is not the same')
    task_list[id] = task

@router.delete('/{id}', status_code=204)
def delete_task(id: int):
    if task_list.get(id) == None:
        raise HTTPException(status_code=404, detail='The task does not exist')
    task_list.pop(id)
