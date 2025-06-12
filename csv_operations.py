import csv

def csv_create(file_path: str):
    """
    Create a CSV file with default headers: 'ID', 'nome', 'cognome', 'codice_fiscale'

    Parameters:
        file_path (str): the path where to save the CSV file.

    """
    columns=["ID","nome","cognome","codice_fiscale"]

    try:
        with open(file_path, mode="w", newline="", encoding="utf-8") as file:
            writer=csv.writer(file)
            writer.writerow(columns)
        print(f"CSV {file_path} created successfully.")
    except Exception as msg:
        print(f"Error creating CSV: {msg}.")
    
def csv_add(file_path: str, record: dict):
    """
    Add a new record to the existing CSV file.

    Parameters:
        file_path (str): the path where to save the CSV file.
        record (dict): dictionary with keys: 'ID', 'nome', 'cognome', 'codice_fiscale'.

    """
    try:
        with open(file_path, mode="a", newline="", encoding="utf-8") as file:
            writer=csv.writer(file)
            writer.writerow([
                record["ID"],
                record["nome"],
                record["cognome"],
                record["codice_fiscale"]
            ])
            print(f"Record with ID {record['ID']} added successfully.")
    except Exception as msg:
        print(f"Error writing record: {msg}.")

def csv_get_records(file_path: str):
    """
    Get all the record from the existing CSV file.

    Parameters:
        file_path (str): the path where to save the CSV file.

    Returns:
        list: all record from

    """
    records=[]
    try:
        with open(file_path, mode="r", newline="", encoding="utf-8") as file:
            reader=csv.DictReader(file)
            records=list(reader)
        return records
    except Exception as msg:
        print(f"Error while getting records: {msg}.")
        return []
    
def csv_get_id(file_path: str, id: str):
    """
    Get a record by ID from the existing CSV file.

    Parameters:
        file_path (str): the path where to save the CSV file.
        id (str): ID of the record to get.

    Returns:
        dict: the record if found, None if not found or in case of error.

    """
    try:
        with open(file_path, mode="r", newline="", encoding="utf-8") as file:
            reader=csv.DictReader(file)
        for i in reader:
            if i["ID"]==id:
                return i        
        print(f"No records found with the id {id}.")
        return None
    except Exception as msg:
        print(f"Error while getting record by ID: {msg}.")
        return None
    
def csv_update(file_path: str, id: str, new_data: dict):
    """
    Update a record, searched by ID, from the existing CSV file.
    Then rewrites all the records in the CSV file to avoid data loss.

    Parameters:
        file_path (str): the path where to save the CSV file.
        id (str): ID of the record to search.
        new_data (dict): a dictionary with keys: 'ID', 'nome', 'cognome', 'codice_fiscale'.

    Returns:
        bool: True if the record was updated successfully, False if not.

    """
    updated=False
    try:
        with open(file_path, mode="r", newline="", encoding="utf-8") as file:
            reader=csv.DictReader(file)
            records=list(reader)
        for i in records:
            if i["ID"]==id:
                i.update(new_data)
                updated=True
                break
        
        if updated==False:
            print(f"No records found with the id {id}.")
            return False
        
        with open(file_path, mode="w", newline="", encoding="utf-8") as file:    
            fieldnames = ["ID", "nome", "cognome", "codice_fiscale"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(records)

        print(f"Record with ID {id} updated successfully.")
        return True
    
    except Exception as msg:
        print(f"Error while updating records: {msg}.")
        return False
    
def csv_delete(file_path: str, id: str):
    """
    Delete a record, searched by ID, from the existing CSV file.
    Then rewrites all the records in the CSV file to avoid data loss.

    Parameters:
        file_path (str): the path where to save the CSV file.
        id (str): ID of the record to search.

    Returns:
        bool: True if the record was deleted successfully, False if not.

    """
    deleted=False
    try:
        with open(file_path, mode="r", newline="", encoding="utf-8") as file:
            reader= csv.DictReader(file)
            records=list(reader)
        for i in records:
            if i["ID"]==id:
                records.remove(i)
                deleted=True
                break

        if deleted==False:
            print(f"No records found with the id {id}.")
            return False
        
        with open(file_path, mode="w", newline="", encoding="utf-8") as file:    
            fieldnames = ["ID", "nome", "cognome", "codice_fiscale"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(records)

        print(f"Record with ID {id} deleted successfully.")
        return True

    except Exception as msg:
        print(f"Error while deleting record: {msg}.")
        return False
    
def csv_get_rows(file_path: str):
    """
    Count rows from the existing CSV file.
    
    Parameters:
        file_path (str): the path where to save the CSV file.

    Returns:
        int: numbers of CSV file's rows.

    """
    cnt=0
    try:
        with open(file_path, mode="r", newline="", encoding="utf-8") as file:
            reader= csv.DictReader(file)
            return sum(1 for _ in reader)
        
    except Exception as msg:
        print(f"Error while counting rows: {msg}.")
        return None