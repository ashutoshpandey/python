# download mysql python connector as zip
# extract the zip and on the command prompt, execute following
# python setup.py install

import mysql.connector
import sys

try:
    con = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='hmssm')

    cursor = con.cursor()
    cursor.execute("SELECT * from courses")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

except mysql.connector.Error as e:

    print("Error %d: %s" % (e.args[0], e.args[1]))
    sys.exit(1)

finally:

    if con:
        con.close()