from pydantic import BaseModel
from csv_operations import *

FILE_PATH = "csv_files/file.csv"

class Item(BaseModel):
    ID: str
    nome: str
    cognome: str
    codice_fiscale: str

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
    
def api_add(item: Item):
    """
    The function adds a new record to the CSV file at the path 'csv_files/file.csv' using the csv_add() utility.

    Parameters:
        item (Item): the new record to add to the CSV file.

    Returns:
        dict: a dictionary that contains a success message or an error message:
            success: {'message': 'New record added to the CSV file','record':'<item>'}
            error: {'error': '<error_message>'}
    """
    try:
        csv_add(FILE_PATH,item)
        return {"message":"New record added to the CSV file","record":item.model_dump()}
    except Exception as msg:
        return {"error": str(msg)}
    
def api_get_records():
    """
    Get all the record from the existing CSV file at the path 'csv_files/file.csv' using the csv_get_records() utility.

    Returns:
        list: all record from the CSV file or a empty list in case of error.

    """
    records=[]
    try:
        records=csv_get_records(FILE_PATH)
        return records
    except Exception as msg:
        return []
    
def api_get_id(id: str):
    """
    Get a record by an ID from the existing CSV file at the path 'csv_files/file.csv' using the csv_get_id() utility.

    Parameters:
        id (str): ID of the record to get.

    Returns:
        dict: the record if found, None if not found or in case of error.

    """
    try:
        return csv_get_id(FILE_PATH, id)
    except Exception as msg:
        return None
    
def api_update(new_item: Item, id: str):
    """
    Update a record searched by an ID from the existing CSV file at the path 'csv_files/file.csv' using the csv_update() utility.

    Parameters:
        new_item (Item): a record with keys: 'ID', 'nome', 'cognome', 'codice_fiscale'.
        id (str): ID of the record to search.

    Returns:
        bool: True if the record was updated successfully, False if not.

    """
    try:
        return csv_update(FILE_PATH, id,new_item)
    except Exception as msg:
        return False
    
def api_delete(id: str):
    """
    Delete a record searched by an ID from the existing CSV file at the path 'csv_files/file.csv' using the csv_delete() utility.

    Parameters:
        file_path (str): the path where to save the CSV file.
        id (str): ID of the record to search.

    Returns:
        bool: True if the record was deleted successfully, False if not.

    """
    try:
        return csv_delete(FILE_PATH, id)
    except Exception as msg:
        return False

def api_get_rows():
    """
    Count rows from the existing CSV file at the path 'csv_files/file.csv' using the csv_get_rows() utility.

    Returns:
        int: numbers of CSV file's rows.

    """
    try:
        return csv_get_rows(FILE_PATH)
    except Exception as msg:
        return None