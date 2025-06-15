from pydantic import BaseModel
from csv_operations import *

FILE_PATH = "csv_files/file.csv"

class Item(BaseModel):
    ID: int
    nome: str
    cognome: str
    codice_fiscale: str

'''
def api_create():
    """
    Create a CSV file with default headers: 'ID', 'nome', 'cognome', 'codice_fiscale'.
    The function creates a CSV file at the path 'csv_files/file.csv' using the csv_create() utility.

    Returns:
        dict: a dictionary that contains a success message or an error message:
            success: {'message': 'CSV file created', 'file': '<file_path>'}
            error: {'error': '<error_message>'}
    """
    try:
        csv_create(FILE_PATH)
        return {"message": "CSV file created", "file":FILE_PATH}
    except Exception as msg:
        return {"error": str(msg)}
'''
    
def api_add(item: Item):
    """
    The function adds a new record to the CSV file at the path 'csv_files/file.csv' using the csv_add() utility.

    Parameters:
        item (Item): the new record to add to the CSV file.

    Returns:
        data (dict): the added recod as a dictionary or a message in case of error.

    """
    try:
        result = csv_add(FILE_PATH,item.model_dump())
        return result
    except Exception as msg:
        return {"error": str(msg)}
    
def api_get_all_records():
    """
    Get all the record from the existing CSV file at the path 'csv_files/file.csv' using the csv_get_records() utility.

    Returns:
        list: all record from the CSV file or a empty list in case of error.

    """
    records=[]
    try:
        records=csv_get_all_records(FILE_PATH)
        return records
    except Exception as msg:
        return []
    
def api_get_id(id: int):
    """
    Get a record by an ID from the existing CSV file at the path 'csv_files/file.csv' using the csv_get_id() utility.

    Parameters:
        id (int): ID of the record to get.

    Returns:
        dict: the record if found, None if not found or in case of error.

    """
    try:
        result = csv_get_id(FILE_PATH, id)
        if result == None:
            return {"Operation result": result}
        else:
            return result
    except Exception as msg:
        return {"error": str(msg)}
    
def api_update(new_item: Item, id: int):
    """
    Update a record searched by an ID from the existing CSV file at the path 'csv_files/file.csv' using the csv_update() utility.

    Parameters:
        new_item (Item): a record with keys: 'ID', 'nome', 'cognome', 'codice_fiscale'.
        id (int): ID of the record to search.

    Returns:
        data (dict): the updated record as a dictionary or a message in case of error.

    """
    try:
        result = csv_update(FILE_PATH, id, new_item)

        if result == None:
            return {"Operation result": result}
        else:
            return result
    except Exception as msg:
        return {"error": str(msg)}
    
def api_delete(id: int):
    """
    Delete a record searched by an ID from the existing CSV file at the path 'csv_files/file.csv' using the csv_delete() utility.

    Parameters:
        file_path (str): the path where to save the CSV file.
        id (int): ID of the record to search.

    Returns:
        dict: a dictionary about the delete result

    """
    try:
        flag = csv_delete(FILE_PATH, id)
        return {"Delete result": flag}
    except Exception as msg:
        return {"Delete result": False}

def api_get_rows():
    """
    Count rows from the existing CSV file at the path 'csv_files/file.csv' using the csv_get_rows() utility.

    Returns:
        int: numbers of CSV file's rows.

    """
    try:
        cnt = csv_get_rows(FILE_PATH)
        return {"Operation result": cnt}
    except Exception as msg:
        return {"error": str(msg)}
