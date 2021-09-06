# import the pymysql module
import pymysql

# Code for creating a connection object
dbServerName    = "127.0.0.1"
dbUser          = "root"
dbPassword      = "01199301"
dbName          = "Bot"
charSet         = "utf8mb4"
cusrorType      = pymysql.cursors.DictCursor


dbConnection   = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword,
                                     db=dbName, charset=charSet,cursorclass=cusrorType)

try:

    # Code for  creating cursor from database connection
    cursorInstance            = dbConnection.cursor()                                    

    id=1
    # SQL statement for deleting rows from a table matching a criteria
    delstatmt = "DELETE FROM `Employee` WHERE id2 = '%s'" % (id,)
    cursorInstance.execute(delstatmt)
    dbConnection.commit()

    # using the cursor delete a set of rows from the table
    #cursorInstance.execute(sqlDeleteRows)
    #print( )

    # Check if there are any existing items with expired status
    sqlSelectRows   = "select * from Employee  WHERE id=3 "

    # Execute the SQL query
    cursorInstance.execute(sqlSelectRows)

    #Fetch all the rows using cursor object
    itemRows = cursorInstance.fetchall()

    # print all the remaining rows after deleting the rows with status as "expired"
    for item in itemRows:
        print(item)   


   

except Exception as ex:

    print("Exception occured: %s"%ex)   

finally:

    dbConnection.close()
