import csv
    
def csv_add(file_path: str, record: dict):
    """
    Add a new record to the existing CSV file.

    Parameters:
        file_path (str): the path where to save the CSV file.
        record (dict): dictionary with keys: 'ID', 'nome', 'cognome', 'codice_fiscale'.
    
    Returns:
        str: a message in case of error.

    """
    try:
        id_list=[]
        with open(file_path, mode="r", newline="", encoding="utf-8") as file:
            records=list(csv.DictReader(file))
            for i in records:
                id_list.append(int(i["ID"]))
            
            if record["ID"] in id_list:
                return {"Operation result": None}

        with open(file_path, mode="a", newline="", encoding="utf-8") as file:
            writer=csv.writer(file)
            writer.writerow([
                record["ID"],
                record["nome"],
                record["cognome"],
                record["codice_fiscale"]
            ])
        return record
    except Exception as msg:
        return {"error":str(msg)}

def csv_get_all_records(file_path: str):
    """
    Get all the record from the existing CSV file.

    Parameters:
        file_path (str): the path where to save the CSV file.

    Returns:
        list: all record from the CSV file or a empty list in case of error.

    """
    records=[]
    try:
        with open(file_path, mode="r", newline="", encoding="utf-8") as file:
            reader=csv.DictReader(file)
            records=list(reader)
        return records
    except Exception:
        return []
    
def csv_get_id(file_path: str, id: int):
    """
    Get a record by ID from the existing CSV file.

    Parameters:
        file_path (str): the path where to save the CSV file.
        id (int): ID of the record to get.

    Returns:
        dict: the record if found, None if not found or a message in case of error.

    """
    try:
        with open(file_path, mode="r", newline="", encoding="utf-8") as file:
            reader=csv.DictReader(file)
            for i in reader:
                if int(i["ID"])==id:
                    return i        
        return None
    except Exception as msg:
        return {"error":str(msg)}
    
def csv_update(file_path: str, id: int, new_data: dict):
    """
    Update a record, searched by ID, from the existing CSV file.
    Then rewrites all the records in the CSV file to avoid data loss.

    Parameters:
        file_path (str): the path where to save the CSV file.
        id (int): ID of the record to search.
        new_data (dict): a dictionary with keys: 'ID', 'nome', 'cognome', 'codice_fiscale'.

    Returns:
        data (dict): the updated record as a dictionary or a message in case of error.

    """
    updated=False
    try:
        with open(file_path, mode="r", newline="", encoding="utf-8") as file:
            reader=csv.DictReader(file)
            records=list(reader)
        for i in records:
            if int(i["ID"])==id:
                i.update(new_data)
                updated_record=i
                updated=True
                break
        
        if updated==False:
            return None
        
        with open(file_path, mode="w", newline="", encoding="utf-8") as file:    
            fieldnames = ["ID", "nome", "cognome", "codice_fiscale"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(records)

        return updated_record
    
    except Exception as msg:
        return {"error": str(msg)}
    
def csv_delete(file_path: str, id: int):
    """
    Delete a record, searched by ID, from the existing CSV file.
    Then rewrites all the records in the CSV file to avoid data loss.

    Parameters:
        file_path (str): the path where to save the CSV file.
        id (int): ID of the record to search.

    Returns:
        bool: True if the record was deleted successfully, False if not.

    """
    deleted=False
    try:
        with open(file_path, mode="r", newline="", encoding="utf-8") as file:
            reader= csv.DictReader(file)
            records=list(reader)
        for i in records:
            if int(i["ID"])==id:
                records.remove(i)
                deleted=True
                break

        if deleted==False:
            return False
        
        with open(file_path, mode="w", newline="", encoding="utf-8") as file:    
            fieldnames = ["ID", "nome", "cognome", "codice_fiscale"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(records)

        return True

    except Exception as msg:
        return False
    
def csv_get_rows(file_path: str):
    """
    Count rows from the existing CSV file.
    
    Parameters:
        file_path (str): the path where to save the CSV file.

    Returns:
        int: numbers of CSV file's rows or a message in case of error.

    """
    cnt=0
    try:
        with open(file_path, mode="r", newline="", encoding="utf-8") as file:
            reader= csv.DictReader(file)
            return len(list(reader))
        
    except Exception as msg:
        return {"error": str(msg)}