# -*- coding: utf-8 -*-
# S E Z A R (1);
# [ Copyright Dev-TALENT (C) All rights reserved 2015 - 2017]

# -( imports )-
import sqlite3

class database:
	def __init__(self):
		self.dbcon=sqlite3.connect('.\connection/dbfile.sqlite')
		self.dbcon.isolation_level=None
		self.dbcon.row_factory=sqlite3.Row
		self.dbcur=self.dbcon.cursor
		self.dbcon.text_factory=str

if __name__ == '__main__':
	self.database()
	print('Database Connection: ON!')
