#!/usr/bin/python2.4
#
# Small script to show PostgreSQL and Pyscopg together
#

import psycopg2

def main():
	print("running")
        conn = psycopg2.connect("dbname='dcfvunds3mi9ke' user='xkfuywemblzisn' host='ec2-50-19-105-113.compute-1.amazonaws.com' password='627a78ad25ed73505ba7af0dbb28eeefb18acb4d6a2c2fd10fe6498c13d99cc9'")
        conn.autocommit = True
        cursor = conn.cursor()
        print("connect")
        sql_query = """CREATE TABLE user_choice (Gender varchar(40) NULL,Age varchar(40) NULL,Country varchar(40) NULL,FavTeam varchar(40) NULL,TimeEntered varchar(30) NULL);"""
        sql_query = """CREATE TABLE player_choice (User_ID varchar(40) NULL,Player_1 varchar(40) NULL,Player_2 varchar(40) NULL,Player_Choice varchar(40) NULL,TimeEntered varchar(30) NULL);"""
        
	cursor.execute(sql_query) 
        #cursor.commit()
        cursor.execute("SELECT * FROM player_choice")
	print("*****************")
	cursor.execute("SELECT * FROM player_choice")
        # retrieve the records from the database
        records = cursor.fetchall()
        print(records)
	
if __name__ == "__main__":
	main()
