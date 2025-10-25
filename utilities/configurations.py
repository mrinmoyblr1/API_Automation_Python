import configparser

import mysql.connector
from mysql.connector import Error


def getConfig():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    # Here the config will be accessed by this config.read() and it will have access on everything under properties.ini file
    return config


connect_config = {
    'user': getConfig()['SQL']['user'],
    'password': getConfig()['SQL']['password'],
    'host': getConfig()['SQL']['host'],
    'database': getConfig()['SQL']['database']
}


def getPassword():
    return "Anjali1234!@#$"


def getConnection():
    try:
        conn = mysql.connector.connect(**connect_config)
        # ** stands for we are mentioning the argument is a Dictionary
        if conn.is_connected():
            print("Connected to MySQL server")
            return conn
    except Error as e:
        print(e)


def getQuery(query):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return row

