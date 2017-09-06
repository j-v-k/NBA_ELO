#!/usr/bin/python2.4
#
# Small script to show PostgreSQL and Pyscopg together
#

import psycopg2

def connect():
    try:
        conn = psycopg2.connect("dbname='dcfvunds3mi9ke' user='xkfuywemblzisn' host='ec2-50-19-105-113.compute-1.amazonaws.com' password='627a78ad25ed73505ba7af0dbb28eeefb18acb4d6a2c2fd10fe6498c13d99cc9'")
        print("connect")
    except:
        print("I am unable to connect to the database")