# download mysql python connector as zip
# extract the zip and on the command prompt, execute following
# python setup.py install

import mysql.connector
import sys

try:
    con = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='hmssm')

    sql = ("INSERT INTO courses "
               "(course_name, course_fees, duration, admin, status, created_at, updated_at) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s)")

    insert_data = ('java++', 5000, '2', 'ashutosh', 'active', '2000-1-1', '2000-1-1')

    cursor = con.cursor()
    cursor.execute(sql, insert_data)

    con.commit()

except mysql.connector.Error as e:

    print("Error %d: %s" % (e.args[0], e.args[1]))
    sys.exit(1)

finally:

    if con:
        con.close()