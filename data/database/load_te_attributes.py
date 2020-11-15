import pandas as pd
import mysql.connector as mariadb
import os
import sys

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

############################################################

# Open metadata file
data = pd.read_csv("../te_attributes.txt", sep="\t")
# Connect to databse
con = mariadb.connect(
            user=os.getenv("USER"),
            host=os.getenv("HOST"),
            password=os.getenv("PASSWORD"),
            database="transposons"
            ) # encapsulate in function
cursor = con.cursor()
# Insert values in parent tables
insert_values(cursor,data.Transposon_Super_Family.unique(), "superFamily", "superFamilyName")
insert_values(cursor,data.orientation_is_5prime.unique(), "orientation", "isFivePrime")
insert_values(cursor,[1,2,3,4,5], "chromosome", "chromosomeNumber")
# Insert values in child tables
for index,row in data.iterrows(): 
    # Insert location, idChromosome and idOrientation in location table
    cursor.execute(f"""INSERT INTO location
        (minStart,maxEnd,idOrientation,idChromosome)
        VALUES(
        {row["Transposon_min_Start"]},
        {row["Transposon_max_End"]},
        (SELECT id FROM orientation WHERE isFivePrime = {row["orientation_is_5prime"]}),
        (SELECT id FROM chromosome WHERE chromosomeNumber = {str(row["Transposon_Name"][2])})
        )
        """)
    # Insert family if not already in table and the corresponding idSuperFamily 
    cursor.execute(f"""INSERT IGNORE INTO family
        (familyName,idSuperFamily)
        VALUES(
        "{row["Transposon_Family"]}",
        (SELECT id FROM superFamily WHERE superFamilyName = "{row["Transposon_Super_Family"]}")
        )
        """)
    # Insert transposon name, idLocation and idFamily in transposon table
    cursor.execute(f"""INSERT IGNORE INTO transposon
        (transposonName,idLocation, idFamily)
        VALUES(
        "{row["Transposon_Name"]}",
        (SELECT id FROM location WHERE minStart = {row["Transposon_min_Start"]}
            AND maxEnd = {row["Transposon_max_End"]}
            AND idChromosome = (SELECT id FROM chromosome WHERE chromosomeNumber = {row["Transposon_Name"][2]})
            AND idOrientation = (SELECT id FROM orientation WHERE isFivePrime = {row["orientation_is_5prime"]})),        
        (SELECT id FROM family WHERE familyName = "{row["Transposon_Family"]}")
        )
        """)
    print(f"{index}/{len(data)} loaded.")
print("End")
con.commit()
cursor.close()
con.close()
