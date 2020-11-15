import pandas as pd
import mysql.connector as mariadb
import os

con = mariadb.connect(
            user=os.getenv("USER"),
            host=os.getenv("HOST"),
            password=os.getenv("PASSWORD"),
            database="transposons"
            ) # encapsulate in function

def insert_values(cursor, values, table,field):
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    rows = cursor.fetchone()[0]
    if int(rows) == 0:
        for value in values:
            if isinstance(value, str):
                cursor.execute(f"""INSERT INTO {table} ({field})
                               VALUES ("{value}")""")
                print(f"Inserted {value} in table {table}.")
            else:
                cursor.execute(f"""INSERT INTO {table} ({field})
                               VALUES ({value})""")
                print(f"Inserted {value} in table {table}.")

    else:
        print(f"{rows} values for {table} already entered.")

metadata = pd.read_csv("../te_attributes.txt", sep="\t")
print(metadata.head())

cursor = con.cursor()
insert_values(cursor,metadata.Transposon_Family.unique(), "family", "familyName")
insert_values(cursor,metadata.Transposon_Super_Family.unique(), "superFamily", "superFamilyName")
insert_values(cursor,metadata.orientation_is_5prime.unique(), "orientation", "isFivePrima")
insert_values(cursor,[1,2,3,4,5], "chromosome", "chromosomeNumber")
con.commit()
cursor.close()
con.close()
