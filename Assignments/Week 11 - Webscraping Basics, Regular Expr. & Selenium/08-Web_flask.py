#!flask/bin/python
from flask import Flask, jsonify, abort, request, json
# dataframe to table
import pymysql

app = Flask(__name__)

# Connect to database
cnx = pymysql.connect(user='dev',
                      password='ax2',
                      host='127.0.0.1',
                      port=3307,
                      db='People')

# Create a cursor object
cursor = cnx.cursor()

# Select data from database
query = ("SELECT ID, NAME FROM People WHERE ID BETWEEN %s and %s")
id_start = 0
id_end = 1000
cursor.execute(query,(id_start, id_end))


# Endpoints


@app.route('/')
def index():
    return "Hello, World from flask server!"


@app.route('/datagenerator/api/persons/<int:no>', methods=['GET'])
def get_tasks(no):
    # Select data from database
    query = ("SELECT * FROM People LIMIT {}").format(no)
    cursor.execute(query)
    print(cursor)
    cursor.close
    persons: object = list()
    for (id, name) in cursor:
        persons.append({'id': "{}".format(id), 'name': "{}".format(name)})
    return jsonify(persons)

@app.route('/datagenerator/api/person', methods=['POST'])
def create_name():
    if not request.json or not 'name' in request.json:
        abort(400)
    query = ("INSERT INTO People(name) VALUES (%s)")
    cursor.execute(query, request.json.get('name', ""))
    cnx.commit()
    print("person successfully added to database")
    select = ("SELECT * FROM People ORDER BY ID DESC LIMIT 1")
    cursor.execute(select)
    result = cursor.fetchone()
    person = {
        'id': result[0],
        'name': result[1]
    }
    return jsonify(person), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0')
