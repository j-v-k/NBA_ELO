import psycopg2

def main():
	
        conn = psycopg2.connect("""dbname='dcfvunds3mi9ke' user='xkfuywemblzisn' host='ec2-50-19-105-113.compute-1.amazonaws.com' password='627a78ad25ed73505ba7af0dbb28eeefb18acb4d6a2c2fd10fe6498c13d99cc9'""")
        conn.autocommit = True
        cursor = conn.cursor()
        print("connect") 
        #cursor.commit()
        cursor.execute("""SELECT * FROM player_choice""")
        
        records = cursor.fetchall()

        
        cursor.execute("""SELECT * FROM user_choice""")
        records = cursor.fetchall()
        print(records)
	
if __name__ == "__main__":
        main()
