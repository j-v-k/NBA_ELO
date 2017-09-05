from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify
import pyodbc
import urllib.parse
import sqlalchemy
import sqlite3
db = SQLAlchemy(app)
#conn = sqlite3.connect(r"C:\Users\James\Documents\GitHub\python_rest\players.db")


#db_connect = create_engine('sqlite:///players.db')
app = Flask(__name__)
api = Api(app)
#cnxn = sqlalchemy.create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted))

class Players(Resource):
    def get(self):
        #conn = db_connect.connect() # connect to database
        #cnxn = pyodbc.connect('DRIVER={MySQL ODBC 5.3 ANSI Driver};SERVER=localhost;PORT=3306;DATABASE=nba_ranking_app;UID=root;PASSWORD=tintin;')
        quoted = urllib.parse.quote('DRIVER={MySQL ODBC 5.3 ANSI Driver};Server=localhost;Database=nba_ranking_app;UID=root;PWD=tintin;TDS_Version=8.0;Port=3306;')
        

        query = cnxn.execute("select * from Players") # This line performs query and returns json result
        return {'players': [i for i in query.cursor.fetchall()]} # Fetches first column that is Player ID

class Players_Name(Resource):
    def get(self, player_id):
        #conn = db_connect.connect()
        #cnxn = pyodbc.connect('DRIVER={MySQL ODBC 5.3 ANSI Driver};SERVER=localhost;PORT=3306;DATABASE=nba_ranking_app;UID=root;PASSWORD=tintin;')
        
        quoted = urllib.parse.quote('DRIVER={MySQL ODBC 5.3 ANSI Driver};Server=localhost;Database=nba_ranking_app;UID=root;PWD=tintin;TDS_Version=8.0;Port=3306;')
        
        query = cnxn.execute("select * from Players where ID =%d "  %int(player_id))
        #file = open(r'C:\Users\James\Documents\GitHub\python_rest\testfile2.txt', 'w')

        #file.write(str(list(query.fetchall())[0]))
        #file.close()
        player_tup = list(query.fetchall())[0]
        player_id = player_tup[0]
        player_name = player_tup[1]
        result = {'ID': player_id , 'Name':player_name}
        return jsonify(result)

class User_Info(Resource):
    def get(self):
        #conn = db_connect.connect() # connect to database
        #cnxn = pyodbc.connect('DRIVER={MySQL ODBC 5.3 ANSI Driver};SERVER=localhost;PORT=3306;DATABASE=nba_ranking_app;UID=root;PASSWORD=tintin;')
        quoted = urllib.parse.quote('DRIVER={MySQL ODBC 5.3 ANSI Driver};Server=localhost;Database=nba_ranking_app;UID=root;PWD=tintin;TDS_Version=8.0;Port=3306;')
        
        query = cnxn.execute("select * from player_chosen") # This line performs query and returns json result
        return {'players': [query.fetchall()]}
    
    def post(self):
        #cnxn = pyodbc.connect('DRIVER={MySQL ODBC 5.3 ANSI Driver};SERVER=localhost;PORT=3306;DATABASE=nba_ranking_app;UID=root;PASSWORD=tintin;')
        quoted = urllib.parse.quote('DRIVER={MySQL ODBC 5.3 ANSI Driver};Server=localhost;Database=nba_ranking_app;UID=root;PWD=tintin;TDS_Version=8.0;Port=3306;')
        
        #conn = db_connect.connect()
        
        #column_list = ['User_ID', 'Gender', 'Age', 'Country', 'FavTeam', 'TimeEntered']
        #column_list= request.
        
        """removes blank values"""
        data_dict = {i: request.json[i] for i in request.json.keys() if request.json[i] != ''}
       
        """gets creates the query to insert into the user info based on the json provided from the post""" 
        qstring =  "INSERT INTO user_info ("
        qstring += ", ".join(list(data_dict.keys())) + ") VALUES ('" + "','".join(list(data_dict.values())) + "')"
        query = cnxn.execute(qstring) # This line performs query and returns json result
        print("Choice Sent")
        
        return {'status':'success','data': request.json}  
    

class Players_Respone(Resource):
    def get(self):
        #conn = db_connect.connect() # connect to database
        #cnxn = pyodbc.connect('DRIVER={MySQL ODBC 5.3 ANSI Driver};SERVER=localhost;PORT=3306;DATABASE=nba_ranking_app;UID=root;PASSWORD=tintin;')
        quoted = urllib.parse.quote('DRIVER={MySQL ODBC 5.3 ANSI Driver};Server=localhost;Database=nba_ranking_app;UID=root;PWD=tintin;TDS_Version=8.0;Port=3306;')
        
        query = cnxn.execute("select * from player_chosen") # This line performs query and returns json result
        return {'players': [query.fetchall()]}
    
    def post(self):
        #cnxn = pyodbc.connect('DRIVER={MySQL ODBC 5.3 ANSI Driver};SERVER=localhost;PORT=3306;DATABASE=nba_ranking_app;UID=root;PASSWORD=tintin;')
        quoted = urllib.parse.quote('DRIVER={MySQL ODBC 5.3 ANSI Driver};Server=localhost;Database=nba_ranking_app;UID=root;PWD=tintin;TDS_Version=8.0;Port=3306;')
        cnxn = sqlalchemy.create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted))
        
        
        #conn = db_connect.connect()
        User_ID = request.json['User_ID']
        Player_1 = request.json['Player_1']
        Player_2 = request.json['Player_2']
        Player_Choice = request.json['Player_Choice']
        TimeEntered = request.json['TimeEntered']
        query = cnxn.execute("INSERT INTO user_choice (User_ID, Player_1, Player_2, Player_Choice, TimeEntered) VALUES ('%s','%s','%s','%s', '%s')" % (str(User_ID), Player_1,Player_2, Player_Choice, TimeEntered)) # This line performs query and returns json result
        print("Choice Sent")
        
        return {'status':'success','data': request.json}  
        
api.add_resource(Players, '/players') # Route_1
api.add_resource(Players_Name, '/players/<player_id>') # Route_3
api.add_resource(Players_Respone, '/Players_Response')
api.add_resource(User_Info, '/User_Info')


if __name__ == '__main__':
     app.run(port='5002')