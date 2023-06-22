import psycopg2
from data_processing import DatatablePreprocess
from sqlalchemy import create_engine
import os


#retrieve an encoded password
from cryptography.fernet import Fernet
key = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY='
cipher_suite = Fernet(key)

with open('postgres.bin', 'rb') as file_object:
    for line in file_object:
        encryptedpwd = line
uncipher_text = (cipher_suite.decrypt(encryptedpwd))
plain_text_encryptedpassword = bytes(uncipher_text).decode("utf-8") 

#connect to the database
conn_string = f'postgresql://postgres:{plain_text_encryptedpassword}@localhost:5432/lifearc'
db = create_engine(conn_string)

conn = db.connect()

#run preprocessing

file_name = 'System_engineer_question3.csv'
file_path = 'data/' + file_name

test = DatatablePreprocess(file_path)

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


#move the uploaded file to a different folder

parent_dir =  'data/'
directory = 'uploaded_data'

path = os.path.join(parent_dir, directory)
try: 
    os.mkdir(path)
    print(path) 
except OSError as error: 
    print(error) 

os.rename(f'data/{file_name}', f'data/uploaded_data/{file_name}')
