
#sudo apt-get install mysql-server
#pip install mysql-connector-python-rf
# import the mysql client for python
#https://pythontic.com/database/mysql/create%20table

import pymysql


# Create a connection object

dbServerName    = "127.0.0.1"
dbUser          = "root"
dbPassword      = "01199301"
dbName          = "Bot"
charSet         = "utf8mb4"
cusrorType      = pymysql.cursors.DictCursor



connectionObject   = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword,
                                     db=dbName, charset=charSet,cursorclass=cusrorType)

try:

    # Create a cursor object
    cursorObject        = connectionObject.cursor()                                     
    # SQL query string
    # https://dev.mysql.com/doc/refman/8.0/en/string-types.html
    # https://dev.mysql.com/doc/refman/8.0/en/date-and-time-types.html

    sqlQuery = "ALTER TABLE `adaptiveV14` ADD NEW_COL copy INT(1) NOT NULL DEFAULT 0 "

# datatype int,    copy int,     timetype int,   t1 int, timestamp DATETIME, startdate DATE, stopdate DATE, time TIME, duration TIME, average_t TIME,

    # Execute the sqlQuery
    cursorObject.execute(sqlQuery)
    # SQL query string
    sqlQuery            = "show tables"   
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery)

    #Fetch all the rows
    rows                = cursorObject.fetchall()
    for row in rows:
        print(row)

except Exception as e:
    print("Exeception occured:{}".format(e))

finally:

    connectionObject.close()
