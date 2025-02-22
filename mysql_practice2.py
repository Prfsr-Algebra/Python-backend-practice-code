#connecting to the database
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Ajala123*45*67",
    database = "practice"
)

#Creating a table
mycursor = mydb.cursor()
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS practice(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE
    )
""")

#Inserting data into the table
sql = "INSERT IGNORE INTO practice (name, email) VALUES (%s, %s)"
val = ("Muhammad", "Muhammad@gmail.com")
mycursor.execute(sql, val)
mydb.commit()
val = ("sulayman", "sulayman@gmail.com")
mycursor.execute(sql, val)
mydb.commit()
print("reading data:")
mycursor.execute("SELECT * from practice")
myresult = mycursor.fetchall()
for i in myresult:
    print (i)

#Manipulating the table
val = ("sul@gmail.com", 1)
sql = "UPDATE practice SET email = %s WHERE id = %s"
mycursor.execute(sql, val)
mydb.commit()
sql = "SELECT * FROM practice WHERE id = %s"
val = (1,)
mycursor.execute(sql, val)
myresult = mycursor.fetchone()
print("the first row after manipulation: ", myresult)

#Deleting from table
sql = "DELETE FROM practice WHERE id = 2"
mycursor.execute(sql)
mydb.commit()
print("total row count after deletion:", mycursor.rowcount)
mycursor.close()
mydb.close()
print("connection closed")