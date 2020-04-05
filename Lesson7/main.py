import sqlite3
conn = sqlite3.connect('employees.db')
cursor = conn.cursor()


cursor.execute(
    f"""
    INSERT INTO employee ('first_name', 'surname', 'salary')
    VALUES ('Anton', 'Polyakov', 1000000)
    """,
)
conn.commit()

for data in cursor:
    print(data)
conn.close()
