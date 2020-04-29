import pymysql
# insert, update, delete

from decimal import Decimal

# Connect with the MySQL Server
cnx = pymysql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='Week1Day4')  
cursor = cnx.cursor()

curA = cnx.cursor()
curB = cnx.cursor()

# Query to get employees who joined in a period defined by two dates
query = ("SELECT ID, SALARY FROM EMPLOYEE WHERE ID BETWEEN 1 AND 3")

# UPDATE and INSERT statements for the old and new salary
update_old_salary = (
  "UPDATE EMPLOYEE SET salary = %s "
  "WHERE id = %s")

# Select the employees getting a raise (all that have id between 1 and 3)
curA.execute(query)

# Iterate through the result of curA
for (id, salary) in curA:
  # Update the old and insert the new salary
  new_salary = int(round(Decimal(salary) * Decimal('1.15')))
  curB.execute(update_old_salary, (new_salary, id))
  # Commit the changes
  cnx.commit()   
  
    
cursor.close()
curA.close()
curB.close()
cnx.close()

cnx = pymysql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='Week1Day4') 

cursor = cnx.cursor(pymysql.cursors.DictCursor) 

query = ("SELECT ID, NAME, ADDRESS, SALARY FROM EMPLOYEE")

cursor.execute(query)
cursor.fetchall()