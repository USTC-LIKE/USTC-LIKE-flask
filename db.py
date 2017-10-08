import sqlite3
import sys

conn=sqlite3.connect('LIKE1.db')
cursor = conn.cursor()

#cursor.execute('select * from paper')
#values= cursor.fetchall()


f = open(sys.argv[1])            
line = f.readline()             
while line:  
    print(line)     
    cursor.execute(line)        
    line = f.readline()  
cursor.execute('select * from PUBLICATION')
values= cursor.fetchall()
print(values)

conn.commit()

cursor.close()
conn.close()

f.close()  
