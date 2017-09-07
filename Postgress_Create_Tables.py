#!/usr/bin/python2.4
#
# Small script to show PostgreSQL and Pyscopg together
#

import psycopg2

def connect():
	conn = psycopg2.connect("dbname='dcfvunds3mi9ke' user='xkfuywemblzisn' host='ec2-50-19-105-113.compute-1.amazonaws.com' password='627a78ad25ed73505ba7af0dbb28eeefb18acb4d6a2c2fd10fe6498c13d99cc9'")
	cursor = conn.cursor()
	print("connect")
	sql_query = "CREATE TABLE dcfvunds3mi9ke.user_info (
	Gender VARCHAR(45) NOT NULL,
	Age VARCHAR(45) NULL,
	Country' VARCHAR(45) NULL,
	FavTeam VARCHAR(45) NULL,
	TimeEntered VARCHAR(45) NULL;"
	cursor.execute(sql_query)
	cursor.commit()
