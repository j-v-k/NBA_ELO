def main():
	print("running")
        conn = psycopg2.connect("""dbname='dcfvunds3mi9ke' user='xkfuywemblzisn' host='ec2-50-19-105-113.compute-1.amazonaws.com' password='627a78ad25ed73505ba7af0dbb28eeefb18acb4d6a2c2fd10fe6498c13d99cc9'""")
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM player_choice""")

        # retrieve the records from the database
        records = cursor.fetchall()
        print(records)
        print("222")
        cursor.execute("""SELECT * FROM user_choice""")
        # retrieve the records from the database
        records = cursor.fetchall()
        print(records)

