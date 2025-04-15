import psycopg2
import csv 

#path
path = "main.csv"
#connection
conn = psycopg2.connect(database = "pp", 
                        user = "postgres",
                        host= 'localhost',
                        password = "3245",
                        port = 5433)

cur = conn.cursor()

#opening table 
cur.execute("""CREATE TABLE IF NOT EXISTS 
            phonebook(id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            phone VARCHAR(20) NOT NULL); """)

name = input("your full name:: ")
phone = input("your phone:: ")

cur.execute("INSERT INTO phonebook(name, phone) VALUES (%s, %s)", (name, phone))

#Opening csv
with open(path) as file:
    csv_reader = csv.reader(file)
    next(csv_reader)

    for line in csv_reader:
        cur.execute("INSERT INTO phonebook(name, phone) VALUES (%s, %s)", (line[1], line[2]))

#Updating data
update = int(input("Wanna update data? (1, 0) "))
if update:
    old_name = input("old_name:: ")
    new_name = input("new_name:: ")

    cur.execute("UPDATE phonebook SET name = %s WHERE name = %s", (new_name, old_name))


#Filtering data
filter_mode = int(input("filter by name or phone? (1, 0) "))
if filter_mode:
    filter_name = input("filter_name:: ")
    cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s", (filter_name,))
else:
    filter_phone = input("filter by phone:: ")
    cur.execute("SELECT * FROM phonebook WHERE phone = %s", (filter_phone,))

rows = cur.fetchall()
for row in rows:
    print(row)

#deleting 
delete = int(input("delete name or phone? (1, 0) "))

if delete:
    delete_name = input("name to delete:: ")
    cur.execute("DELETE FROM phonebook WHERE name = %s", (delete_name,))
else:
    delete_phone = input("phone to delete:: ")
    cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))

conn.commit()

cur.close()
conn.close()