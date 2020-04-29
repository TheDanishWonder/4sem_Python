import pymysql

# Connect to database
cnx = pymysql.connect(user='dev',
                      password='ax2',
                      host='127.0.0.1',
                      port=3307,
                      db='Cars')

# Create a cursor object
cursor = cnx.cursor()

#---------------------------------------------#
# If the table doesnt exist do this only once!
## SQL query string
# newTable = "CREATE TABLE Cars(Make varchar(32), Model varchar(32), Year int, Price int)"
#try:
## Execute the sqlQuery
#    cursor.execute(newTable)

## Throw exeception if failed
# except Exception as e:
#    print("Exeception occured:{}".format(e))

# finally:
## Close connection    
#    cursor.close()
#--------------------------------------------#

# dataframe to table
import pandas as pd
from sqlalchemy.engine import create_engine

#cnx = pymysql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='Cars') 
con_str = 'mysql+pymysql://dev:ax2@localhost:3307/Cars'
engine = create_engine(con_str)

df = pd.DataFrame({'Make' : ['VW', 'Audi', 'Citroen'],
                  'Model':['UP','A6', 'C3'],
                  'Year':['2018','2011','2019'],
                  'Price':['123000', '85000', '143000']})
#df = df.applymap(str)
df.to_sql('Cars',con=engine, if_exists='append', index = False)
print(df.dtypes)