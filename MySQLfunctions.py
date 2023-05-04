from mysql.connector import *
mydb=connect(user="root",host="localhost",passwd="s1j1H3a45%$")
cursor=mydb.cursor()
cursor.execute("use test")
def create():
    cursor.execute("create table userdata(usernumber integer primary key,username varchar(20),emailid varchar(20),score integer)")
def write(username,email):
    command="insert into userdata(usernumber,username,emailid,score) values(%s,%s,%s,%s)"
    values=(1,username,email,0)
    cursor.execute(command,values)
    mydb.commit()

