import mysql.connector
 
mydb = mysql.connector.connect(host='127.0.0.1',username='root',passwd='123456789',database='school',autocommit= True )

cursor = mydb.cursor()
 
cursor.execute("insert into class1(name,age,reg,marks,city)values('smith',20,26,78,'bangalore')") 