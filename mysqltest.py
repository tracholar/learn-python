# coding:utf8
import MySQLdb as mysql

try:
	conn = mysql.connect('202.38.79.161','root','123456','english')
	cur = conn.cursor()
	count = cur.execute('select count(*) from think_message')
	result = cur.fetchall()
	print count,'\n',result[0][0]
	cur.close()
	conn.close()
	
except mysql.Error, e :
	print e