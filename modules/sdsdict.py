# sds compile dictonory

# 3rd-party
import sqlite3
from constants import DB_CONN

def sds():
	sdsdict = {
		'month': '',
		'year': '',
		'firstline': '',
		'issues': '',
	}
	c = DB_CONN.cursor()
	c.execute('SELECT pro_month, pro_year, pro_firstline, pro_issues FROM production WHERE pro_id = 1')
	rows = c.fetchall()
	for pro_month, pro_year, pro_firstline, pro_issues in rows:
		sdsdict['month'] = pro_month
		sdsdict['year'] = pro_year
		sdsdict['firstline'] = pro_firstline
		sdsdict['issues'] = pro_issues
	c.close()
	return sdsdict