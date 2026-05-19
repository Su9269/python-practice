import pandas as pd
import sqlite3

df = pd.DataFrame({
    "employee": ["Amy", "John", "Eric", "Tom"],
    "department": ["Sales", "Sales", "Tech", "Tech"],
    "performance": [80, 50, 95, 40],
    "salary": [50000, 40000, 100000, 35000]
})

conn = sqlite3.connect("test.db")

df.to_sql(
    "employee",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("database created!")
