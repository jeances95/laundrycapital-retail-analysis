import pandas as pd
import os
from sqlalchemy import create_engine

# -----------------------------
# FILE PATHS (robust handling)
# -----------------------------
base_path = os.path.join(os.getcwd(), "data", "raw")

customers_path = os.path.join(base_path, "customers_laundrycapital.xlsx")
stores_path = os.path.join(base_path, "stores_laundrycapital.xlsx")
services_path = os.path.join(base_path, "services_laundrycapital.xlsx")
sales_path = os.path.join(base_path, "sales_laundrycapital.xlsx")

# -----------------------------
# LOAD DATA
# -----------------------------
customers = pd.read_excel(customers_path)
stores = pd.read_excel(stores_path)
services = pd.read_excel(services_path)
sales = pd.read_excel(sales_path)

print("Files loaded successfully")

# -----------------------------
# CLEANING FUNCTION
# -----------------------------
def clean_columns(df):
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    return df

customers = clean_columns(customers)
stores = clean_columns(stores)
services = clean_columns(services)
sales = clean_columns(sales)

# Remove duplicates
customers = customers.drop_duplicates()
stores = stores.drop_duplicates()
services = services.drop_duplicates()
sales = sales.drop_duplicates()

# Handle missing values
customers = customers.fillna("Unknown")
stores = stores.fillna("Unknown")
services = services.fillna("Unknown")
sales = sales.fillna(0)

print("Data cleaned successfully")

# -----------------------------
# SQL SERVER CONNECTION
# -----------------------------
server = 'localhost'   # change if needed
database = 'LaundryCapitalDB'

connection_string = f"mssql+pyodbc://@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"

engine = create_engine(connection_string)

# -----------------------------
# LOAD TO SQL SERVER
# -----------------------------
customers.to_sql("dim_customers", engine, if_exists="replace", index=False)
stores.to_sql("dim_stores", engine, if_exists="replace", index=False)
services.to_sql("dim_services", engine, if_exists="replace", index=False)
sales.to_sql("fact_sales", engine, if_exists="replace", index=False)

print("ETL completed successfully 🚀")