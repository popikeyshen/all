
# import the mysql client for python
# https://pymysql.readthedocs.io/en/latest/user/examples.html

import pymysql


# Create a connection object

# Connect to the database
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
    sqlQuery            = "select * from Employee"

    # Execute the sqlQuery
    cursorObject.execute(sqlQuery)

    #Fetch all the rows
    rows                = cursorObject.fetchall()

    for row in rows:
        print(row["id"],row["id2"],row["plan"])
        #print(row["id2"])   
  

except Exception as e:

    print("Exeception occured:{}".format(e))

finally:

    connectionObject.close()
