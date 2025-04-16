import psycopg2
import csv

#connecting to SQL
conn = psycopg2.connect(
    database="postgres",
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

#adding contact
def add_contact():
    name = input("Select Name: ").strip()
    phone = input("Select Number: ").strip()
    try:
        cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
        conn.commit()
        print("Contact added.")
    except psycopg2.errors.UniqueViolation:
        conn.rollback()
        print("Number already exists")
    except Exception as e:
        conn.rollback()
        print("Something wrong", e)

#importing
def import_from_csv():
    path = input("Show path to CSV:").strip() or "main.csv"
    try:
        with open(path, newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Пропуск заголовка
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
    old_name = input("Old name: ").strip()
    new_name = input("New name: ").strip()
    cur.execute("UPDATE phonebook SET name = %s WHERE name = %s", (new_name, old_name))
    conn.commit()
    print("Name updated")


#deleting
def delete():
    choice = input("Delete by name (1) or number (2)?: ").strip()
    if choice == "1":
        name = input("Select name: ").strip()
        cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
    elif choice == "2":
        phone = input("Select number: ").strip()
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    else:
        print("That's wrong ")
        return
    conn.commit()
    print("Done")

#main meny
def main():
    while True:
        print("\n PhoneBook Menu:")
        print("1. Add contact")
        print("2. Import from CSV")
        print("3. Update name")
        print("4. Find")
        print("5. Deleting")
        print("0. Exit")
        choice = input("Your choice:").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            import_from_csv()
        elif choice == "3":
            update_name()
        elif choice == "4":
            search()
        elif choice == "5":
            delete()
        elif choice == "0":
            print("Goodbye")
            break
        else:
            print("Something's wrong.")

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
