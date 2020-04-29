import pymysql

cnx = pymysql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='Week1Day4')  

cursor = cnx.cursor()

query = ("SELECT NAME, ID, SALARY FROM EMPLOYEE WHERE id BETWEEN %s AND %s")

id_start = 1
id_end = 10

cursor.execute(query, (id_start, id_end))

for (NAME, ID, SALARY) in cursor:
    print("{} has id number {} and the employees salary is paid: {} DKR pr month".format(NAME, ID, SALARY))

cursor.close()
cnx.close()