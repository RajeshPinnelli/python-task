import mysql.connector as myconn
mydb=myconn.connect(host="localhost",user="root",password="Rajesh@1")
print("connection established",mydb)
db_cursor=mydb.cursor()
db_cursor.execute("create database  Student")
print("Databse Created")
mydb=myconn.connect(host="localhost",user="root",password="Rajesh@1",database="student")
db_cursor=mydb.cursor()
db_cursor.execute("""create table Students (
                  student_id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            age INT,
            grade FLOAT)""")
print("table created")

db_cursor.execute("show tables")
for i in db_cursor:
    print(i)
db_cursor.execute("INSERT INTO Students (first_name, last_name, age, grade) VALUES (%s, %s, %s, %s)",("Alice", "Smith",18,95.5))
mydb.commit()
print(db_cursor.rowcount,"Records Inserted")
db_updated="UPDATE Students SET grade = %s WHERE first_name = %s"
values = (97.0,"Alice" )
db_cursor.execute(db_updated, values)
mydb.commit()
print(db_cursor.rowcount,"Data updated")


db_delete = "DELETE FROM Students WHERE last_name = %s"
values = ("Smith",)
db_cursor.execute(db_delete, values)
mydb.commit()
print(db_cursor.rowcount,"Data Deleted")

db_cursor.execute("SELECT * FROM Students")
result = db_cursor.fetchall()
for row in result:
        print(row,"fected  all data")
mydb.close()


