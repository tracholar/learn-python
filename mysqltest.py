# coding:utf8
import MySQLdb as mysql

try:
	conn = mysql.connect('localhost','root','123456','english')
	cur = conn.cursor()
	count = cur.execute('select count(*) from tuofu')
	result = cur.fetchall()
	print count,'\n',result[0][0]
	cur.close()
	conn.close()
	
except mysql.Error, e :
	print e