import sqlite3


#В данном коде мы создали класс, который берет путь к файлу базы данных SQLite Python.
# Метод __enter__ выполняется автоматически, он создает и возвращает объект связи базы данных.
# Теперь мы можем создать курсор для записи в базу данных или чтобы её запросить.
# Когда мы выходим из оператора with, метод __exit__ запускается, закрывая таким образом связь.
class DataConn:

    def __init__(self, db_name):
        """Конструктор"""
        self.db_name = db_name

    def __enter__(self):
        """
        Открываем подключение с базой данных.
        """
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Закрываем подключение.
        """
        self.conn.close()
        if exc_val:
            raise

if __name__ == '__main__':
    db = 'employees.db'

with DataConn(db) as conn:
    cursor = conn.cursor()
    cursor.execute(
    f"""
        SELECT * FROM emloyee
    """
    )
    for data in cursor:
        print(data)
