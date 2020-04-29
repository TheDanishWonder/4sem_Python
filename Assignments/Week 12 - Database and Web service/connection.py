import pandas as pd
import pymysql
from sqlalchemy import create_engine

data = pd.read_csv("befkbhalderstatkode.csv")

name = "statskode"
print("DATA:\n", data)

username = "root"
password = "root"
ip = "localhost"
port = "3306"
database = "pythonexercisetwo"

connection_string = 'mysql+pymysql://' + username + ':' + password + \
    '@' + ip + ':'+port+'/'+database + '?charset=utf8mb4'
print(connection_string)

engine = create_engine(connection_string)

connection = pymysql.connect(
    host=ip, user=username, password=password, db=database)

data.to_sql(name, engine, if_exists='replace', index=False)

sql_query = f'SELECT * FROM {name}'

with connection.cursor() as cursor:
    
    cursor.execute(sql_query)
    
    for i in cursor.fetchall():
        print(i)
