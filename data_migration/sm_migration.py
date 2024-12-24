from config.db_config import get_db_connection
import pandas as pd
import numpy as np

def migration():
    # Define the Excel file path
    file_path = "Geotech_DB.xlsx"
    
    # Read the Excel sheet into a DataFrame
    sm = pd.read_excel(file_path, sheet_name="Shotcrete_Mix")
    
    # Replace NaN with None (which translates to NULL in MySQL)
    sm = sm.where(pd.notnull(sm), None)
    
    # Rename the columns to remove parentheses, percentages, and spaces, replacing them with underscores
    sm.columns = sm.columns.str.replace(r'[\(\)%]', '', regex=True).str.replace(' ', '_')

    # Convert the 'Date' column to the proper format 'YYYY-MM-DD'
    sm['Date'] = pd.to_datetime(sm['Date'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')

     # Clean the columns that are expected to be float
    def clean_numeric_column(col):
        # Replace any non-numeric or 'None' values with NaN, then convert to float
        return pd.to_numeric(sm[col], errors='coerce')  # 'coerce' turns non-numeric into NaN
    
    # Clean the relevant numeric columns
    sm['Superplasticiser_kg'] = clean_numeric_column('Superplasticiser_kg')
    sm['Accelerator_'] = clean_numeric_column('Accelerator_')
    sm['Fines_Moisture_'] = clean_numeric_column('Fines_Moisture_')
    sm['Coarse_Moisture_'] = clean_numeric_column('Coarse_Moisture_')
    sm['Cement:Water_Ratio'] = clean_numeric_column('Cement:Water_Ratio')
    sm['Cubic_M'] = clean_numeric_column('Cubic_M')
    sm['Fines_kg'] = clean_numeric_column('Fines_kg')
    sm['Coarse_kg'] = clean_numeric_column('Coarse_kg')
    sm['Cement_kg'] = clean_numeric_column('Cement_kg')
    sm['Water_kg'] = clean_numeric_column('Water_kg')
    sm['Add_1_Fines_kg'] = clean_numeric_column('Add_1_Fines_kg')
    sm['Add_1_Coarse_kg'] = clean_numeric_column('Add_1_Coarse_kg')
    sm['Add_1_Cement_kg'] = clean_numeric_column('Add_1_Cement_kg')
    sm['Add_1_Water_kg'] = clean_numeric_column('Add_1_Water_kg')
    sm['Add_1_Superplasticiser_kg'] = clean_numeric_column('Add_1_Superplasticiser_kg')
    sm['Add_2_Fines_kg'] = clean_numeric_column('Add_2_Fines_kg')
    sm['Add_2_Coarse_kg'] = clean_numeric_column('Add_2_Coarse_kg')
    sm['Add_2_Cement_kg'] = clean_numeric_column('Add_2_Cement_kg')
    sm['Add_2_Water_kg'] = clean_numeric_column('Add_2_Water_kg')
    sm['Add_2_Superplasticiser_kg'] = clean_numeric_column('Add_2_Superplasticiser_kg')
    sm['Fibre_kg'] = clean_numeric_column('Fibre_kg')


    # Step 1: Save the cleaned DataFrame to a CSV file
    csv_file_path = "Shotcrete_Mix_Data.csv"
    sm.to_csv(csv_file_path, index=False)

    # Step 2: Read the CSV file back (This simulates the step of migrating from CSV to MySQL)
    sm_from_csv = pd.read_csv(csv_file_path)

    # Get the database connection
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        
        # Prepare the INSERT INTO query for MySQL with the new column names
        query = """
            INSERT INTO shotcrete_mix (
                `FACE_ID`, `Date`, `Start_Time`, `Batch_Number`, `Fines_kg`, `Fines_Moisture_`, `Coarse_kg`,
                `Coarse_Moisture_`, `Cement_kg`, `Water_kg`, `Cement:Water_Ratio`, `Cubic_M`, 
                `Superplasticiser_kg`, `Accelerator_`, `Fibre_kg`, `Additive_1_kg`, `Add_1_Fines_kg`,
                `Add_1_Coarse_kg`, `Add_1_Cement_kg`, `Add_1_Water_kg`, `Add_1_Superplasticiser_kg`,
                `Add_2_Fines_kg`, `Add_2_Coarse_kg`, `Add_2_Cement_kg`, `Add_2_Water_kg`,
                `Add_2_Superplasticiser_kg`
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        
        # Step 3: Iterate over each row in the DataFrame (from CSV) and insert into MySQL
        for index, row in sm_from_csv.iterrows():
            # Map the DataFrame row to a tuple (replace NaN with None)
            data_tuple = tuple(None if pd.isna(value) else value for value in row)
            data_tuple = tuple(None if pd.isna(value) or value == ' ' else value for value in row)

            
            # Execute the query to insert the data into MySQL
            cursor.execute(query, data_tuple)
        
        # Commit the transaction
        connection.commit()
        print("Data migration completed successfully.")
        
        # Close the cursor and connection
        cursor.close()
        connection.close()

# Run the migration
migration()
