import pandas as pd
import sqlite3

df = pd.DataFrame({
    "employee": ["Amy", "John", "Eric", "Tom", "Kevin", "Mary", "David", "Jenny", "Mike", "Cindy"],
    "department": ["Sales", "Sales", "Tech", "Tech", "Tech", "HR", "HR", "Sales", "Finance", "Finance"],
    "performance": [80, 50, 95, 40, 70, 85, 60, 75, 88, 45],
    "salary": [50000, 40000, 100000, 35000, 65000, 70000, 45000, 55000, 90000, 42000],
    "years": [2, 1, 5, 1, 3, 4, 2, 3, 6, 1]
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
