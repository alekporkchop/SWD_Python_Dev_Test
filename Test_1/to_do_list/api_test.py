import requests

def GetAllToDo():

    response = requests.get('http://127.0.0.1:8000/to_do_list/')
    return response.json()

def GetToDo(id):

    response = requests.get('http://127.0.0.1:8000/to_do_list/{}'.format(id))
    return response.json()

toDoData = {
    "title": "get some drinks",
    "description": "stay hydrated :)",
    "completed": False,
}

def CreateToDo(data):
    response = requests.post('http://127.0.0.1:8000/to_do_list/', json=data)
    return response.json()


editToDo = {
    "description": "Done",
    "completed": True,
}

def EditToDo(id, data):
    response = requests.put('http://127.0.0.1:8000/to_do_list/{}'.format(id), json=data)
    return response.json()


def DeleteToDo(id):
    response = requests.delete('http://127.0.0.1:8000/to_do_list/{}'.format(id))
    return response.status_code

print(GetAllToDo())
print(GetToDo(1))
print(GetToDo(3)) #not found
print(CreateToDo(toDoData))
allToDo = GetAllToDo()
lastestTodo = allToDo[len(allToDo) -1]
print(EditToDo(lastestTodo.id, editToDo))
print(DeleteToDo(lastestTodo.id))