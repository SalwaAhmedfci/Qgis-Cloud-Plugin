from random import random

import psycopg2
import Connection_Strings as creds
import string
import random
import requests
import VisionCloud
import enum
from User_db import *


# Using enum class create enumerations


def get_random_string():
    length = creds.LENGTH
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def Request_Database_Creation(token):
    URL = creds.DATABASE_REQUEST_URL
    param = 'Bearer' + " " + token
    # sending get request and saving the response as response object

    r = requests.get(url=URL, headers={'Authorization': param})
    #json_data = json.dumps(r, default=lambda o: o.__dict__, indent=4)
    # VisionCloud.list_of_databases.append(r.text)
    re = r.json()
    
    return re




def connection():
    # Set up a connection to the postgres server.
    conn_string = "host=" + creds.HOST + " port=" + "5432" + " dbname=" + creds.DATABASE + " user=" + creds.USER \
                  + " password=" + creds.PASSWORD
    try:
        conn = psycopg2.connect(conn_string)
        print("Connected!")

        # Create a cursor object
        cursor = conn.cursor()

        def load_data(schema, table):

            sql_command = "SELECT * FROM {}.{};".format(str(schema), str(table))
            print(sql_command)

            # Load the data
            data = pd.read_sql(sql_command, conn)

            print(data.shape)
            return data




    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
