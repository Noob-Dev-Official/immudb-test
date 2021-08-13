import library
import uuid
import uuid_to_hex as uth


def transaction(amount, trans_type):
   # conn = library.db()

   # my_test = f"INSERT INTO POSTING (id, amount, type) VALUES ('{str(uuid.uuid4())}', {amount}, '{trans_type}')"
   # # print(my_test)
   # # conn.run(f"INSERT INTO POSTING (id, amount, type) VALUES ('sddsffsd23432', {amount}, '{trans_type}')")

   # conn.run("INSERT INTO POSTING (id, amount, type) VALUES ('a1454f1b-5424-4881-b301-204c85f86a68', 4342, 'deposit')")

   # conn, cur = library.db()

   # # cur.execute("BEGIN TRANSACTION")
   # cur.execute("INSERT INTO POSTING (id, amount, type) VALUES ('sdg353', 4342, 'deposit');")
   # # cur.execute("END TRANSACTION")

   # conn.commit()

   client = library.db()

   print(uth.uuid_to_hex('62ed479a-df3d-4db8-9d63-ef153f8303ff'))

   client.sqlExec("INSERT INTO test (id) VALUES (@id)", {'id': str(uth.uuid_to_hex(uuid.uuid4()))})

   test_data = client.sqlQuery('select * from test')
   print(test_data)