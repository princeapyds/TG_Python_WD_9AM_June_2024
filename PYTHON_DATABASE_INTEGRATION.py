import sqlite3 # import SQlite database library
connection = sqlite3.connect("sample.db") # create a database named Sample/
cursor = connection.cursor() # open cursor , to execute commands
cursor.execute("CREATE TABLE if not exists customers (cust_id text, name text, address text, contact text)")
cursor.execute("INSERT INTO customers VALUES ( 'customer1','Amit Patil' , 'Pune' , '989898')")
print(list(cursor.execute("SELECT * FROM customers ")))
cursor.execute("INSERT INTO customers VALUES ( 'customer2','Sumit Patil' , 'Mumbai' , '121133')")
print(list(cursor.execute("SELECT * FROM customers ")))
cursor.execute("UPDATE customers set address= 'Mumbai' where  cust_id = 'customer1'")
print(list(cursor.execute("SELECT * FROM customers ")))
cursor.execute("DELETE FROM customers where cust_id = 'customer1'")
print(list(cursor.execute("SELECT * FROM customers ")))

