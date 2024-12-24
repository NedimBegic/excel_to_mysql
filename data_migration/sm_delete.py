from config.db_config import get_db_connection



def delete_all_records(table_name):
    """
    Deletes all records from the specified table in the database.

    Args:
        table_name (str): The name of the table to clear.
    """
    # Get the database connection
    connection = get_db_connection()
    if connection:
        try:
            # Create a cursor object
            cursor = connection.cursor()
            
            # SQL query to delete all records
            query = f"DELETE FROM {table_name};"
            
            # Execute the query
            cursor.execute(query)
            
            # Commit the transaction
            connection.commit()
            print(f"All records have been deleted from the table '{table_name}'.")
        
        except Exception as e:
            print(f"An error occurred while deleting records: {e}")
        
        finally:
            # Close the cursor and connection
            cursor.close()
            connection.close()

# Example usage
# delete_all_records("shotcrete_mix")
table = "shotcrete_mix"
delete_all_records(table)