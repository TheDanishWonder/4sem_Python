import pymysql

def getNames(statement):

    connection = pymysql.connect(
        user='root', password='root', host='127.0.0.1', port=3306, db='pythonexercise')

    with connection.cursor() as cursor:

        query = (statement)

        cursor.execute(query)

        for(firstname, lastname) in cursor:
            print("First Name:", firstname)
            print("Last Name:", lastname)
            print("")

        print("This is sent to MySQL:", cursor._last_executed)

    connection.close()


# 1.
print("\nPersoner som har en salary der er højere end 50.000\n")
getNames('SELECT firstname, lastname FROM pythonexercise.pythondemo WHERE salary>50000;')
# 2.
print("\nPersoner som har efternavnet 'Juhlborg'\n")
getNames('SELECT `firstname`, `lastname` FROM pythonexercise.pythondemo WHERE lastname="Juhlborg";')
