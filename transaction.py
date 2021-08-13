import library
import uuid



def transaction(amount, trans_type):
   conn = library.db()

   my_test = f"INSERT INTO POSTING (id, amount, type) VALUES ('{str(uuid.uuid4())}', {amount}, '{trans_type}')"
   # print(my_test)
   # conn.run(f"INSERT INTO POSTING (id, amount, type) VALUES ('sddsffsd23432', {amount}, '{trans_type}')")

   conn.run("INSERT INTO POSTING (id, amount, type) VALUES ('a1454f1b-5424-4881-b301-204c85f86a68', 4342, 'deposit')")

   # conn, cur = library.db()

   # cur.execute("INSERT INTO POSTING (id, amount, type) VALUES ('sdg353', 4342, 'deposit')")

   # conn.commit()