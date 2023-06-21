import psycopg2
from data_processing import DatatablePreprocess
from sqlalchemy import create_engine


conn_string = 'postgresql://postgres:postgres@localhost:5432/lifearc'
db = create_engine(conn_string)

conn = db.connect()

file_name = 'data/System_engineer_question3.csv'

test = DatatablePreprocess(file_name)

process_test = test.run_datatable_preprocess()

process_test.to_sql('antibodies', con=conn, if_exists='replace',
          index=False)


conn = psycopg2.connect(conn_string
                        )

conn.autocommit = True
cursor = conn.cursor()
  
sql1 = '''select * from antibodies;'''
cursor.execute(sql1)

for i in cursor.fetchall():
    print(i)





