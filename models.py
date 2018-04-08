import os
import sqlite3 as sql

DB_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)),'database.db')

def create_tables():
    con = sql.connect(DB_PATH)
    cur = con.cursor()
    try:
        cur.execute('CREATE TABLE IF NOT EXISTS locations(search_id INTEGER PRIMARY KEY, location_name text NOT NULL, longitude INTEGER NOT NULL, latitude INTEGER NOT NULL)')
        cur.execute('INSERT INTO locations(location_name,longitude,latitude) VALUES(?,?,?)',('Sydney',151.209900,-33.865143))
        cur.execute('INSERT INTO locations(location_name,longitude,latitude) VALUES(?,?,?)',('New York',73.935242,40.730610))
        con.commit()
        con.close()
    except:
        print('table locations already exists')

def save_location(name, lon, lat):
    con = sql.connect(DB_PATH)
    cur = con.cursor()
    cur.execute('INSERT INTO locations(location_name,longitude,latitude) VALUES(?,?,?)',(name,lon,lat))
    con.commit()
    con.close()

def get_locations():
    con = sql.connect(DB_PATH)
    cur = con.cursor()
    cur.execute('SELECT * FROM locations')
    locations = cur.fetchall()
    con.close()
    return locations

def get_location(loc_id):
    con = sql.connect(DB_PATH)
    cur = con.cursor()
    cur.execute('SELECT * FROM locations WHERE search_id={}'.format(loc_id))
    location = cur.fetchall()
    con.close()
    return location

