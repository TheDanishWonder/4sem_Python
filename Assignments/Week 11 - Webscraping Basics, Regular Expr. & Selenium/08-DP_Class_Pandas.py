import pandas as pd 
import pymysql

cnx = pymysql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='Week1Day4') 

df = pd.read_sql('SELECT * FROM EMPLOYEE', con=cnx)
df

# dataframe to table
import pandas as pd 
import pymysql
from sqlalchemy.engine import create_engine

#cnx = pymysql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='Week1Day4') 
con_str = 'mysql+pymysql://dev:ax2@localhost:3307/Week1Day4'
engine = create_engine(con_str)

df = pd.DataFrame({'ADDRESS' : ['Central Avenue 234', 'Portland street 12', 'Colgate street 2352'],
                  'NAME':['Blake','Willman','Tessa'],
                  'salary':['21000', '32000', '43000']})
#df = df.applymap(str)
df.to_sql('EMPLOYEE',con=engine, if_exists='append', index = False)
print(df.dtypes)