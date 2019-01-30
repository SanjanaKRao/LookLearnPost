"""import mysql.connector

cnx = mysql.connector.connect(user='root',password='sanjana',
                              host='127.0.0.1',
                              database='test')
cnx.close()
print('Working?')
import mysql

#!/usr/bin/python

#import mysql
import mysql.connector

# Open database connection
#db = mysql.connector.connect("localhost","root","sanjana","test" )
db= mysql.connector.connect(user='sanjkrao',password='sanjana',
                              host='127.0.0.1',
                              database='test')
# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)

sql="SELECT * FROM student"

cursor.execute(sql)
results = cursor.fetchall()
print(results)
for row in results:
      id = row[0]
      name = row[1]
      class1 = row[2]
      
      # Now print fetched result
      print("id=%d,name=%s,class1=%d" % (id,name,class1))

# disconnect from server
db.close()

##flask part
from flask import Flask
app=Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

if __name__== "__main__":
    app.run()   

    # Import `tensorflow`
import tensorflow as tf

# Initialize two constants
x1 = tf.constant([1,2,3,4])
x2 = tf.constant([5,6,7,8])

# Multiply
result = tf.multiply(x1, x2)

# Print the result
print(result) """
import subprocess
def shll():
    #cmd=["ls","-l","/home"]
    cmd = ["docker","run","-v","$PWD:/opt/app","-e","PYTHONPATH=$PYTHONPATH:/opt/app","-it","medium-show-and-tell-caption-generator", "python3","/opt/app/medium_show_and_tell_caption_generator/inference.py","--model_path","/opt/app/etc/show-and-tell.pb","--input_files","/opt/app/imgs/\"01\".jpg","--vocab_file","/opt/app/etc/word_counts.txt"]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    print(cmd)
    out,err = p.communicate()
    print(out)
shll()