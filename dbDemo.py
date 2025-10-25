from utilities.configurations import getConnection

conn = getConnection()
print(conn.is_connected())

cursor = conn.cursor()
# In Python, .cursor() is a method used with database connection objects.
# It creates a cursor object, which is essential for executing SQL queries and
# managing the results from a database.
# Think of the cursor as your "controller" for the database.

cursor.execute('select * from CustomerInfo')

# row = cursor.fetchone()
# print(row)
# print(row[3])
rows = cursor.fetchall()
print(type(rows))
print(rows)

sum = 0
for row in rows:
    sum = sum + row[2]

print(sum)
assert sum == 403

# Update Statement
query = "update customerInfo set Location = %s where CourseName = %s"
# Creating a tuple data and passing the data tuple through argument of cursor.execute()
# Here %s will be replaced by data from data tuple
data = ('UK', 'JMeter')
print(type(data))
cursor.execute(query, data)
conn.commit()  # Always need to perform commit after any Insert/Update/Delete operation

# Delete Statement
deleteQuery = "delete from customerInfo where courseName = 'WebServices'"
cursor.execute(deleteQuery)
conn.commit()

# Insert Statement
insertQuery = "INSERT INTO CustomerInfo values('WebServices',CURRENT_DATE(),21,'Asia');"
cursor.execute(insertQuery)
conn.commit()

conn.close()
