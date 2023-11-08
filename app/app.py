from fastapi import FastAPI

app = FastAPI()


# minimal app -- get request
@app.get("/", tags=['ROOT'])
async def root() -> dict:
    return {"ping": "pong"}


# GET --> read todo
@app.get('/todo', tags=['todos'])
async def get_todo() -> dict:
    return {"data": todos}


# POST --> create todo
@app.post("/todo", tags=["todos"])
async def add_todo(todo: dict) -> dict:
    todos.append(todo)
    return {
        "data": "A todo has been added!"
    }


# PUT --> update todo
@app.put("/todo{id}", tags=["todos"])
async def update_todo(id: int, body: dict) -> dict:
    for todo in todos:
        if int((todo["id"])) == id:
            todo["Activity"] = body['Activity']
            return {
                "data": f"Todo with {id} has been updated"
            }
    return {
        "data": f"Todo with this id number {id}was not found !"
    }


# DELETE --> delete todo
@app.delete("/todo/{id}", tags=["todos"])
async def delete_todo(id: int) -> dict:
    for todo in todos:
        if int((todo["id"])) == id:
            todos.remove(todo)
            return {
                "data": f"todo wit id {id} has been deleted."
            }
    return {
        "data": f"this todo with id {id} wasn't found!"
    }


todos = [
    {
        "id": "1",
        "Activity": "Jogging for 2 hours at 7:00 AM."
    },
    {
        "id": "2",
        "Activity": "Writing 3 pages of my new book at 2:00 PM."
    }
]
