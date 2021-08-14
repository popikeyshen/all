# https://pythontic.com/database/mysql

import pymysql

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='01199301',
                             db='Bot',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `Employee` (`id`, `id2`, `plan`, `full_plan`, `Datetime`) VALUES (%s, %s, %s, %s, %s)"
	full_plan="change world"
	plan="2 plan"
        cursor.execute(sql, ('3', '5',plan,full_plan,'1970-01-01 08:00:00'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id2`, `plan`,`full_plan`,`Datetime` FROM `Employee` WHERE `id`=%s"
        cursor.execute(sql, ('3'))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
