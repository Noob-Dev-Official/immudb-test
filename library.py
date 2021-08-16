# import pg8000.native
# import psycopg2
from immudb import ImmudbClient

 
def db():
   # conn = pg8000.native.Connection(
   #    user="immudb", 
   #    host="localhost", 
   #    password="immudb", 
   #    database="defaultdb",
   #    port="5430"
   # )

   # return conn

   # conn = psycopg2.connect(
   #    host="localhost",
   #    database="defaultdb",
   #    user="immudb",
   #    password="immudb",
   #    port="5430",
   #    sslmode="disable"
   # )

   # cur = conn.cursor()

   # return conn, cur

   client = ImmudbClient()
   client.login('immudb', 'immudb')

   return client

if __name__ == "__main__":
   db()