<!DOCTYPE html>
<html>
<head>
</head>
<body>
    <h1>Excel to MySQL Migration Tool</h1>
    <p>
        This project is a Python-based utility designed to migrate data from an Excel database to a MySQL database. 
        The migration process involves converting the Excel file into a CSV format and then importing the cleaned 
        and structured data into MySQL.
    </p>
    
   <h2>Features</h2>
    <ul>
        <li>Reads data from an Excel file using <strong>Pandas</strong>.</li>
        <li>Cleans and preprocesses the data to ensure compatibility with MySQL:
            <ul>
                <li>Handles invalid numeric values.</li>
                <li>Converts date formats into MySQL-compatible formats.</li>
                <li>Replaces non-numeric entries with <code>NULL</code> where necessary.</li>
            </ul>
        </li>
        <li>Saves the processed data into a CSV file.</li>
        <li>Imports the cleaned data from the CSV file into a MySQL table.</li>
        <li>Includes functionality to delete all rows from the target MySQL table if needed.</li>
    </ul>
    
   <h2>Prerequisites</h2>
    <p>To use this project, you need to have the following installed:</p>
    <ul>
        <li>Python 3.7 or higher</li>
        <li>MySQL Server</li>
        <li>Required Python libraries (see below)</li>
    </ul>
    
  <h2>Dependencies</h2>
    <p>The project uses the following Python libraries:</p>
    <ul>
        <li><code>pandas</code>: For reading, processing, and cleaning the Excel data.</li>
        <li><code>numpy</code>: For handling missing or invalid data.</li>
        <li><code>pymysql</code>: For connecting to the MySQL database.</li>
        <li><code>python-dotenv</code>: For securely managing database credentials.</li>
    </ul>
    <p>Install these dependencies using:</p>
    <pre><code>pip install pandas numpy pymysql python-dotenv</code></pre>
    
   <h2>How It Works</h2>
    <h3>Excel to CSV Conversion:</h3>
    <ul>
        <li>The script reads data from an Excel file (<code>Geotech_DB.xlsx</code>) and preprocesses it to ensure compatibility with MySQL.</li>
        <li>The processed data is saved into a CSV file (<code>Shotcrete_Mix_Data.csv</code>).</li>
    </ul>
    <h3>CSV to MySQL Migration:</h3>
    <ul>
        <li>The script reads the CSV file and inserts its data into a MySQL table.</li>
        <li>Columns in the table are automatically mapped to the CSV columns.</li>
    </ul>
    <h3>Database Operations:</h3>
    <ul>
        <li>The project includes a function to delete all rows from the MySQL table, allowing for a fresh migration when needed.</li>
    </ul>
    
   <h2>Configuration</h2>
    <p>Create a <code>.env</code> file in the project directory to securely store your MySQL credentials:</p>
    <pre><code>DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=your_database_name
</code></pre>
    <p>Make sure <code>.env</code> is listed in your <code>.gitignore</code> file to prevent it from being uploaded to version control.</p>
    
  <h2>Running the Project</h2>
    <ol>
        <li>Clone the repository and navigate to the project directory:
            <pre><code>git clone &lt;repository-url&gt;
cd &lt;project-directory&gt;
</code></pre>
        </li>
        <li>Run the migration script:
            <pre><code>python migration.py</code></pre>
        </li>
        <li>To delete all rows from the MySQL table before running the migration, call the <code>delete_table_data()</code> function in the appropriate script.</li>
    </ol>
    
   <h2>Folder Structure</h2>
    <pre><code>project/
│
├── config/
│   └── db_config.py        # Contains the database connection logic
├── Geotech_DB.xlsx         # Example Excel file for migration
├── Shotcrete_Mix_Data.csv  # Processed CSV file
├── migration.py            # Main migration script
├── utils.py                # Utility functions like deleting rows
├── .env                    # Environment file for storing credentials
├── .gitignore              # Ensures sensitive files are not committed
└── README.md               # Project documentation
</code></pre>
    
  <h2>Example Usage</h2>
    <ol>
        <li>Place your Excel file (<code>Geotech_DB.xlsx</code>) in the project directory.</li>
        <li>Run the <code>migration.py</code> script to convert the Excel file to CSV and import it into MySQL.</li>
    </ol>
    
  <h2>Notes</h2>
    <ul>
        <li>Ensure your MySQL table structure matches the columns in the CSV file.</li>
        <li>Non-numeric or invalid data is replaced with <code>NULL</code> to prevent errors during migration.</li>
    </ul>
</body>
</html>
