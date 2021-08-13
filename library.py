import pg8000.native
import psycopg2

 
def db():
   conn = pg8000.native.Connection(
      user="immudb", 
      host="localhost", 
      password="immudb", 
      database="defaultdb",
      port="5430"
   )

   return conn

   # conn = psycopg2.connect(
   #    host="localhost",
   #    database="defaultdb",
   #    user="immudb",
   #    password="immudb",
   #    port="5431"
   # )

   # cur = conn.cursor()

   # return conn, cur