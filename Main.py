import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345",
    database="mydatabase"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# mycursor.execute("DESCRIBE customers")

# for x in mycursor:
#     print(x)

# persons = [("Chathusha", "Galle"), ("Renuja", "Panadura"), ("Senodth", "Galle"),("Udula", "Pannipitiya"),("Navod","Kaduwela")]

# for person in persons:
#     mycursor.execute("INSERT INTO customers (name, address) VALUES(%s, %s)", person)

# mydb.commit()

# mycursor.execute("SELECT * FROM customers")

# for x in mycursor:
#     print(x)
