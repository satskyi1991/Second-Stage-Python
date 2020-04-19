import sqlite3
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

Administrator =1
User = 2
role = 0
UserAction = 0
AdminAction = 0
while role != 3:
    role = int(input('Choose actions:\n'
                    '1 - Administrator \n'
                    '2 - User \n'
                    '3 - exit:\n'))
    if role == Administrator:
        while AdminAction != 3:
            AdminAction = int(input('Choose actions:\n'
                         '1 - Add student \n'
                         '2 - Change Student information \n'
                         '3 - exit:\n'))
            if AdminAction == 1:
                name = str(input('Enter name:'))
                surname = str(input('Enter surname:'))
                faculty = str(input('Enter faculty:'))
                party = str(input('Enter group:'))
                id = str(input('Enter id:'))
                mark = int(input('Enter mark:'))

                cursor.execute(
                    """
                        INSERT INTO students('name', 'surname', 'faculty', 'party', 'id', 'mark')
                        VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    [name, surname, faculty, party, id, mark]
                )
                conn.commit()

            elif AdminAction == 2:
                name = str(input('Enter name:'))
                surname = str(input('Enter surname:'))
                faculty = str(input('Enter faculty:'))
                party = str(input('Enter group:'))
                id = str(input('Enter id:'))
                mark = int(input('Enter mark:'))

                cursor.execute(
                    """
                    UPDATE students
                    SET name = ?, surname= ?, faculty = ?, party = ?, mark = ?
                    WHERE id = ?
                    """,
                    [name, surname, faculty, party, mark, id]
                )
                conn.commit()
            else:
                break

    elif role == User:
        while User != 5:
            UserAction = int(input('Choose actions:\n'
                '1 - Get list of Excellent students\n'
                '2 - Get list of students\n'
                '3 - Get student by id number\n'
                '4 - Get student information\n'
                '5 - exit\n'))
            if (UserAction == 1):
                cursor.execute(
                    f"""
                    SELECT name, surname FROM students
                    WHERE mark == ?
                    """,
                    [5]
                )
                for data in cursor:
                    print(data)
            elif(UserAction == 2):
                cursor.execute(
                f"""
                    SELECT name, surname FROM students
                """
                )
                for data in cursor:
                    print(data)
            elif(UserAction == 3):
                id = str(input('Enter id:'))
                cursor.execute(
                    f"""
                    SELECT name, surname FROM students
                    WHERE id == ?
                    """,
                    [id]
                    )
                for data in cursor:
                    print(data)
            elif(UserAction == 4):
                id = str(input('Enter id:'))
                cursor.execute(
                    f"""
                    SELECT * FROM students
                    WHERE id == ?
                    """,
                    [id]
                )
                for data in cursor:
                    print(data)
            else:
                break
    else:
        break



conn.close()
