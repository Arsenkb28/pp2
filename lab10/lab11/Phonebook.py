import psycopg2
import csv

#connecting to SQL
conn = psycopg2.connect(
    database="phonebook;",
    user="postgres",
    password="1234",
    host="localhost",
    port=5432
)
cur = conn.cursor()

#creating table if its not exist
cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        phone VARCHAR(20) NOT NULL UNIQUE
    );
""")

conn.commit()


#2 task

def add_or_update_contact():
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    try:
        # Вызов процедуры для добавления или обновления контакта
        cur.callproc('add_or_update_contact', (name, phone))  # передаем параметры как кортеж
        conn.commit()
        print("Контакт добавлен или обновлен.")
    except Exception as e:
        conn.rollback()
        print("Ошибка при добавлении или обновлении контакта:", e)

#importing
def import_from_csv():
    path = "main.csv"
    try:
        with open(path, newline='') as file:
            reader = csv.reader(file)
            next(reader)  #skil the name
            for row in reader:
                try:
                    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (row[1], row[2]))
                except psycopg2.errors.UniqueViolation:
                    conn.rollback()
                else:
                    conn.commit()
        print("Import is done.")
    except Exception as e:
        print("Mistake while reading CSV:", e)

#updating
def update_name():
    old_name = input("Old name: ")
    new_name = input("New name: ")
    cur.execute("UPDATE phonebook SET name = %s WHERE name = %s", (new_name, old_name))
    conn.commit()
    print("Name updated")
#update number
def insert_or_update_user():
    name = input()
    phone = input()
    cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
    conn.commit()


# 1 task finding by pattern
def search():
    choice = input("Finding by name (1) or number (2)? ")

    if choice == "1":
        name = input("Select name: ")
        cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s", (f"%{name}%",))
    elif choice == "2":
        phone = input("Select number: ")
        cur.execute("SELECT * FROM phonebook WHERE phone = %s", (phone,))
    else:
        print("Wrong choice")
        return

    rows = cur.fetchall()
    if rows:
        print("Founded!")
        for row in rows:
            print(row)
    else:
        print("Nothing founded.")



def ask_for_pagdata():
    limit = input("limit- ")
    offset = input("offset- ")

    try:
        limit = int(limit)
        offset = int(offset)

        cur.execute("SELECT * FROM phonebook ORDER BY id LIMIT %s OFFSET %s", (limit, offset))
        rows = cur.fetchall()

        if rows:
            for row in rows:
                print(row)
        else:
            print("there is nothing")

    except ValueError:
        print("Integers for limit and offset")

#main meny
def main():
    while True:
        print("\n PhoneBook Menu:")
        print("1. Find(1-task)")
        print("9. Import from CSV")
        print("3. Update name")
        print("6. Update number")
        print("10. Pagination(2-task)")

        print("0. Exit")
        choice = input("Your choice:")
        if choice == "2":
            add_or_update_contact()
        elif choice == "9":
            import_from_csv()
        elif choice == "3":
            update_name()
        elif choice == "1":
            search()

        elif choice == "6":
            insert_or_update_user()
        elif choice == "10":
            ask_for_pagdata()
        elif choice == "0":
            print("Goodbye")
            break
        else:
            print("Something's wrong.")

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()



