
import sqlite3

conn = sqlite3.connect('employees.db')
cursor = conn.cursor()

# value = input('enter value')
# cursor.execute(
#     f"""
#     DELETE FROM emloyee
#     WHERE emloyee.id > 7
#     """
# )
# # conn.commit()

cursor.execute(
    f"""
    INSERT INTO emloyee('first_name', 'Surname', 'salary')
    VALUES ('Illia', 'Satskyi', '3300')
    """
)
conn.commit()

# INSERT INTO emloyee('first_name', 'Surname', 'salary')
# VALUES ('Illia', 'Satskyi', '3300')
# SELECT * FROM emloyee
# WHERE salary > ?
for data in cursor:
    print(data)

#cursor.fetchone()
conn.close()
