#!/usr/bin/python2.4
#
# Small script to show PostgreSQL and Pyscopg together
#

import psycopg2

def main():
	print("running")
        conn = psycopg2.connect("dbname='initdb' user='postgres' host='localhost' password='tintin'")
        conn.autocommit = True
        cursor = conn.cursor()
        print("connect")
        sql_query1 = """CREATE TABLE user_choice (Gender varchar(40) NULL,Age varchar(40) NULL,Country varchar(40) NULL,FavTeam varchar(40) NULL,TimeEntered varchar(30) NULL);"""
        sql_query2 = """CREATE TABLE player_choice (User_ID varchar(40) NULL,Player_1 varchar(40) NULL,Player_2 varchar(40) NULL,Player_Choice varchar(40) NULL,TimeEntered varchar(30) NULL);"""
        cursor.execute(sql_query1)
	cursor.execute(sql_query2) 		
        #cursor.commit()
        cursor.execute("SELECT * FROM player_choice")
	print("*****************")
	cursor.execute("SELECT * FROM player_choice")
        # retrieve the records from the database
        records = cursor.fetchall()
        print(records)
	
if __name__ == "__main__":
        main()
