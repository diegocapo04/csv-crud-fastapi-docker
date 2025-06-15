from fastapi import FastAPI
from api_operations import *
app = FastAPI()   

# curl.exe -X POST "http://127.0.0.1:8000/items/" -H "Content-Type: application/json" -d '{\"ID\": 2, \"nome\": \"Mario\", \"cognome\": \"Rossi\", \"codice_fiscale\": \"BBB\"}'
@app.post("/items/")
def add_new_record(item: Item):
    item=api_add(item)     
    return item

# curl.exe -X GET "http://localhost:8000/items/count/"
@app.get("/items/count/")
def get_rows_count():
    cnt=api_get_rows()
    return cnt

# curl.exe -X GET "http://localhost:8000/items/1"
@app.get("/items/{id}")
def get_record_by_id(id: int):
    record = api_get_id(id)
    print(id)
    print(record)
    return record

# curl.exe -X PUT "http://127.0.0.1:8000/items/1" -H "Content-Type: application/json" -d '{\"ID\": 1, \"nome\": \"Mario\", \"cognome\": \"Rossi\", \"codice_fiscale\": \"BBB\"}'
@app.put("/items/{id}")
def update_record(item: Item, id: int):
    item=api_update(item,id)
    return item

# curl.exe -X DELETE "http://localhost:8000/items/1"
@app.delete("/items/{id}")
def delete_record(id: int):
    flag = api_delete(id)
    return flag

# curl.exe -X GET "http://localhost:8000/items/"
@app.get("/items/")
def get_all_records():  
    records = api_get_all_records()
    return records