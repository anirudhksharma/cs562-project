import subprocess


def main():
    """

    
    This is the generator code. It should take in the MF structure and generate the code
    needed to run the query. That generated code should be saved to a 
    file (e.g. _generated.py) and then run.
    """

    body = """
    import pandas as pd
    import numpy as np
    from collections import defaultdict


    query = "SELECT * FROM Sales;"  # Replace 'Sales' with your table name
    df = pd.read_sql_query(query, con=cur.connection)
    column_name = "quant"  # Replace 'quantity' with your column name

    # Step 3: Calculate aggregate functions
    min_value = int(df[column_name].min())
    max_value = int(df[column_name].max())
    avg_value = int(df[column_name].mean())
    sum_value = int(df[column_name].sum())
    count_value = int(df[column_name].count())

    

    # Step 4: Prepare results for display
    
    print(avg_value) 

    def process_scans(cur):
    
    
    
        # Step 1: Prompt the user for values of S, n, V, F, sigma
        S = input("Enter SELECT statement columns (comma-separated): ").split(',')
        S = [col.strip() for col in S]

        n= int(input("Enter the number of grouping variables (n): "))

        V = input("Enter GROUP BY attributes (comma-separated): ").split(',')
        V = [col.strip() for col in V]

        F = input("Enter aggregate functions (comma-separated, e.g., sum(X.quantity)): ").split(',')
        F = [func.strip() for func in F]
        

        #sigma = input("Enter 'such that' conditions (comma-separated): ").split(',')
        #sigma = [cond.strip() for cond in sigma]
        #sigma = []
        #print("Enter conditions for each grouping variable in the 'such that' clause:")
        #for i in range(1, n + 1):
         #   condition = input(f"Condition for grouping variable {i}: ").strip()
          #  sigma.append(condition)

        column_string = ", ".join(V)  # Format as "col1, col2, col3"
        query_string = f"SELECT DISTINCT {column_string} FROM sales"    

        
    
        
        try:
            # Step 2: Execute a SELECT query to fetch all rows (tuples) from the Sales table
            cur.execute(query_string)
            rows = cur.fetchall()

            # Step 3: Loop over each tuple t in the result
            print("Looping over each tuple in the Sales table:")
            for t in rows:
                # Ensure t['quant'] is not a list, extract its value if needed
                quant_value = t['quant']
                if isinstance(quant_value, list):  # If 'quant' is a list, take the first element
                    quant_value = quant_value[0]

                if quant_value > avg_value and t['month'] == 3:
                    _global.append(t)  # Append row to global list if condition is satisfied

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            # Ensure the cursor and connection are closed
            cur.close()
            conn.close()

        #results = defaultdict(lambda: defaultdict(float))
            
        #print("Fetching data from the table...")
        #cur.execute("SELECT * FROM sales")
        #rows = cur.fetchall()
          
    process_scans(cur)
    """


    # Note: The f allows formatting with variables.
    #       Also, note the indentation is preserved.
    tmp = f"""
import os
import psycopg2
import psycopg2.extras
import tabulate
from dotenv import load_dotenv

# DO NOT EDIT THIS FILE, IT IS GENERATED BY generator.py

def query():
    load_dotenv()

    user = os.getenv('USER')
    password = os.getenv('PASSWORD')
    dbname = os.getenv('DBNAME')

    conn = psycopg2.connect("dbname="+dbname+" user="+user+" password="+password,
                            cursor_factory=psycopg2.extras.DictCursor)
    cur = conn.cursor()
    cur.execute("SELECT * FROM sales")
    
    _global = []
    {body}
    
    return tabulate.tabulate(_global,
                        headers="keys", tablefmt="psql")

def main():
    print(query())
    
if "__main__" == __name__:
    main()
    """

    # Write the generated code to a file
    open("_generated.py", "w").write(tmp)
    # Execute the generated code
    subprocess.run(["python", "_generated.py"])


if "__main__" == __name__:
    main()
