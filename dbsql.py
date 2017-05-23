# -*- coding: utf-8 -*-
# S E Z A R (1);
# [ Copyright Dev-TALENT (C) All rights reserved 2015 - 2017]

# -( imports )-
import sqlite3

class dbsql:
	def __init__():
		dbcon=sqlite3.connect('.\connection/dbfile.sqlite')
		dbcon.isolation_level=None
		dbcon.row_factory=sqlite3.Row
		dbcur=self.dbcon.cursor
		dbcon.text_factory=str

if __name__ == '__main__':
	dbsql()
	print('Database Connection: ON!')
