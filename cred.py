import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()


DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")


def findAll():

	conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
	cur = conn.cursor()
	cur.execute("SELECT * FROM stickers ORDER BY counter ASC")
	print(cur.fetchall())
	conn.close()


def findbyId(id):

	conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
	cur = conn.cursor()
	cur.execute("SELECT s FROM stickers s WHERE s.id=" + id + " ORDER BY counter ASC")
	print(cur.fetchall())
	conn.close()


def update(id,counter):

	conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
	cur = conn.cursor()
	sql = """ UPDATE stickers
                SET counter = %s
                WHERE id = %s"""
	cur.execute(sql, (id,counter))
	conn.commit()
	cur.close()
	conn.close()
