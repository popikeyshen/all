


# sudo pip install enum
# sudo pip install pymysql
# https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-16-04
# sudo apt-get install mysql-server
# nohup /usr/bin/python2.7 -u /home/pi/katebot/server_v2.py &>logfile &

import pymysql
import datetime
import uuid

# how copy database
# mysqldump -u root -p -f Bot > /home/popikeyshen/mydbdump.sql
#------------------------------
# 1.on new pc - create
# mysql -u root -p
# CREATE DATABASE Bot;
# quit

# 2.remake
# mysql -u root -p -f Bot < /home/popikeyshen/mydbdump.sql

connection = pymysql.connect(host='localhost',
                             user='',
                             password='',
                             db='Bot',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)





# debug read all
def readall():
	try:
		cursor = connection.cursor()
		#sql = " select * from `adaptiveV15` "#WHERE `id`=%s"
		#sql = "SELECT `short` FROM `adaptiveV15` "#WHERE `id`=%s"
		sql = " SELECT `user`,`short`, `startdate`, `stopdate`, `time`, `price`,`graph_at`, `id`, `graph_to`,`priority`, `tasktype`, `archived` FROM `adaptiveV15` "#WHERE `id`=%s"
        	#cursor.execute(sql, ('1',))
		cursor.execute(sql,)
		#result = cursor.fetchone()
		result = cursor.fetchall()
		#print(result["plan"])
		ret=""
		for row in result:
			ret += str(row["short"])
			ret += "\n"
			ret += "user= "+str(row["user"])+" | tasktype="+str(row["tasktype"])+" | from="+str(row["graph_at"])+" id="+str(row["id"])+" to="+str(row["graph_to"])+" | archived="+str(row["archived"])+" | price="+str(row["price"])+" | priority="+str(row["priority"]) 

			ret += "\n"
			ret += str(row["startdate"]).partition(' ')[0]+"  "+str(row["stopdate"]).partition(' ')[0]+"  "+str(row["time"]).partition(' ')[0]
			ret += "\n\n"
		return ret

	except Exception as e:
		print("mysql error readall:{}".format(e))

# function - read
def mysqlReadList(user_id):  
	try:
		cursor = connection.cursor()
		sql = " select short from `adaptiveV15` WHERE (`archived` != 1) "#WHERE `id`=%s"
		cursor.execute(sql,)
		result = cursor.fetchall()
		ret=""
		i=0
		for row in result:
			#ret+=str(row)
			i+=1
			ret+=str(i)+") "
			ret+=str(row["short"])
			ret+="\n"
		return ret

	except Exception as e:
		print("mysql error ReadList:{}".format(e))

def mysqlSetPriority(user_id,graph_to,priority):
	try:

		cursor = connection.cursor()
		sql   = "UPDATE `adaptiveV15` SET  priority=%s WHERE user =%s AND id =%s"
		cursor.execute(sql, (priority, str(user_id), graph_to))
		connection.commit()

		return str(priority)+" is done"

	except Exception as e:
		print("mysql error mysqlSetPriority:{}".format(e))

# function - read
def mysqlReadPriority(user_id):  
	try:
			cursor = connection.cursor()
			sql = " select short,price,timetype,copy,time,priority from `adaptiveV15` WHERE `user` =%s AND (`priority` != 0) AND (`archived` != 1) ORDER BY priority ASC "#WHERE `id`=%s"
			cursor.execute(sql, (str(user_id)) )
			result = cursor.fetchall()

			ret=""
			i=0
			for row in result:

				i+=1
				ret+=str(i)+") "

				if(str(row["price"]) is not "0" ):
					ret+=" $"+str(row["price"])+" "

				ret+=str(row["short"])+" "

				if(str(row["timetype"]) == "1"):
					ret+="(a) "
				#if(str(row["timetype"]) == "0"):
				#	ret+="(h) "

				if(str(row["copy"]) == "1"):
					ret+="(e) "

				#if(str(row["priority"]) != "0"):
				#	ret+="("+str(row["priority"])+") "

				if(str(row["time"]) != "0:00:00"):
					ret+=" "+str(row["time"])

				ret+="\n"

			return ret



	except Exception as e:
		print("mysql error ReadGraph:{}".format(e))


# function - read
def mysqlReadGraph(user_id, graph_at=0):  
	try:

		if graph_at == "1" :
			cursor = connection.cursor()
			sql = " select short,price,timetype,copy,time, timestamp, priority from `adaptiveV15` WHERE `user` =%s AND (`archived` != 1) AND `graph_at`=%s ORDER BY timestamp DESC "#WHERE `id`=%s"
			cursor.execute(sql, (str(user_id), graph_at) )
			result = cursor.fetchall()



			ret=""
			i=0
			timestamp="0"
			for row in result:

				if timestamp != str(row["timestamp"]).partition(' ')[0]:
					timestamp = str(row["timestamp"]).partition(' ')[0]
					ret+="\n----"+timestamp+"---\n"

				i+=1
				ret+=str(i)+") "

				if(str(row["price"]) is not "0" ):
					ret+=" $"+str(row["price"])+" "

				ret+=str(row["short"])+" "

				if(str(row["timetype"]) == "1"):
					ret+="(a) "
				#if(str(row["timetype"]) == "0"):
				#	ret+="(h) "

				if(str(row["copy"]) == "1"):
					ret+="(e) "

				if(str(row["time"]) != "0:00:00"):
					ret+="\t\t"+str(row["time"])

				ret+="\n"			
				

			return ret
		else:
			cursor = connection.cursor()
			sql = " select short,price,timetype,copy,time,priority from `adaptiveV15` WHERE `user` =%s AND (`archived` != 1) AND `graph_at`=%s  ORDER BY timestamp ASC"#WHERE `id`=%s"
			cursor.execute(sql, (str(user_id), graph_at) )
			result = cursor.fetchall()

			ret=""
			i=0
			for row in result:

				i+=1
				ret+=str(i)+") "

				if(str(row["price"]) is not "0" ):
					ret+=" $"+str(row["price"])+" "

				ret+=str(row["short"])+" "

				if(str(row["timetype"]) == "1"):
					ret+="(a) "
				#if(str(row["timetype"]) == "0"):
				#	ret+="(h) "

				if(str(row["copy"]) == "1"):
					ret+="(e) "

				if(str(row["priority"]) != "0"):
					ret+="("+str(row["priority"])+") "

				if(str(row["time"]) != "0:00:00"):
					ret+=" "+str(row["time"])

				ret+="\n"

			return ret



	except Exception as e:
		print("mysql error ReadGraph:{}".format(e))

# function - readfull
def mysqlReadGraphFull(user_id, graph_at=0):  
	try:
		cursor = connection.cursor()
		sql = " select `user`,`short`, `timestamp`, `startdate`, `stopdate`, `time`, `price`,`graph_at`, `id`, `graph_to`,`priority`, `tasktype`, `archived` from `adaptiveV15` WHERE `user` =%s AND (`archived` != 1) AND `graph_at`=%s ORDER BY timestamp ASC "#WHERE `id`=%s"
		cursor.execute(sql, (str(user_id), graph_at) )
		result = cursor.fetchall()
		ret=""
		i=0
		for row in result:
			ret += str(row["short"])
			ret += "\n"
			ret += "user= "+str(row["user"])+" | tasktype="+str(row["tasktype"])+" | from="+str(row["graph_at"])+" id="+str(row["id"])+" to="+str(row["graph_to"])+" | archived="+str(row["archived"])+" | price="+str(row["price"])+" | priority="+str(row["priority"]) 

			ret += "\n"
			#ret += str(row["startdate"]).partition(' ')[0]+"  "+str(row["stopdate"]).partition(' ')[0]+"  "+str(row["time"]).partition(' ')[0]
			ret += str(row["timestamp"])+" "+ str(row["startdate"])+"  "+str(row["stopdate"])+"  "+str(row["time"])
			ret += "\n\n"

			ret+="\n"
		return ret

	except Exception as e:
		print("mysql error ReadGraph:{}".format(e))


# 
def mysqlAutoCopyToPool(user_id, graph_at=0 ):
	try:
		#print "copytopool"
		#print graph_at
		#print user

		cursor = connection.cursor()
		sql = " select `user`,`short`, `startdate`, `stopdate`, `time`, `price`,`graph_at`, `id`, `graph_to`,`priority`, `tasktype`, `archived` from `adaptiveV15` WHERE `user` =%s AND (`archived` != 1) AND `graph_at`=%s "#WHERE `id`=%s"
		cursor = connection.cursor()
		sql = " select id from `adaptiveV15` WHERE `archived`!=1 AND `user`=%s AND  `graph_at`=%s "#WHERE `id`=%s"
		
		cursor.execute(sql, (str(user_id), graph_at) )
		result = cursor.fetchall()
		i=0
		ret=""
		for row in result:
			#ret+=str(row)
			i+=1
			ret=str(row["id"])

			print ret

		#row = result[0]
		#print(str(row))

		#for row in result:
			#ret += str(row["short"])
			#ret += "\n"
			#ret += "user= "+str(row["user"])+" | tasktype="+str(row["tasktype"])+" | from="+str(row["graph_at"])+" id="+str(row["id"])+" to="+str(row["graph_to"])+" | archived="+str(row["archived"])+" | price="+str(row["price"])+" | priority="+str(row["priority"]) 

			#ret += "\n"
			#ret += str(row["startdate"]).partition(' ')[0]+"  "+str(row["stopdate"]).partition(' ')[0]+"  "+str(row["time"]).partition(' ')[0]
			#ret += str(row["startdate"])+"  "+str(row["stopdate"])+"  "+str(row["time"])
			#ret += "\n\n"

			#ret+="\n"
		print ret

		#(user_id,text,stopdate,graph_at='0',price='0', graph_to='0',tasktype='0',priority='0',full="0",datatype='0',timetype='0',startdate="1970-01-01",time="0",duration="0")

		#mysqlAddToList(str(row["user"]),str(row["short"]),str(row["stopdate"]),2,str(row["price"]),str(row["graph_to"]),str(row["tasktype"]),str(row["priority"]),str(row["full"]),str(row["datatype"]),str(row["timetype"]),str(row["startdate"]),str(row["time"]),str(row["duration"]) )
		

		#return response
	except Exception as e:
		print("mysql error mysqlAutoCopyToPool:{}".format(e))


# read graph of task number
def mysqlGraphN(user_id,n, graph_at=0):  
	try:
		cursor = connection.cursor()
		sql = " select id from `adaptiveV15` WHERE `archived`!=1 AND `user`=%s AND  `graph_at`=%s  ORDER BY timestamp ASC"#WHERE `id`=%s"
		
		cursor.execute(sql, (str(user_id), graph_at) )
		result = cursor.fetchall()
		i=0
		for row in result:
			#ret+=str(row)
			i+=1
			ret=str(row["id"])
			if i == n:
				return ret
		return ""

	except Exception as e:
		print("mysql error GraphN:{}".format(e))

def mysqlBackGraph(user_id, graph_id):  
	try:
		# an error if you read empty
		cursor = connection.cursor()
		sql = " select graph_at from `adaptiveV15` WHERE (`archived` != 1) AND `user`=%s AND  `id`=%s "#WHERE `id`=%s"
		cursor.execute(sql, (str(user_id), graph_id) )
		result = cursor.fetchall()
		i=0
		for row in result:
			#ret+=str(row)
			i+=1
			ret=str(row["graph_at"])
			if i == 1:
				return ret
		return ""

	except Exception as e:
		print("mysql error BackGraph:{}".format(e))


def mysqlAddToList(user_id,text,stopdate,graph_at='0',price='0', graph_to='0',tasktype='0',priority='0',full="0",datatype='0',timetype='0',startdate="1970-01-01",time="0",duration="0"):
	#print("debug1")
	try:
		cursor = connection.cursor()
		sql  = "INSERT INTO `adaptiveV15` (user, tasktype, priority, graph_at, id, graph_to, short, full, datatype, timetype, copy, t1, timestamp, startdate, stopdate, time, duration, price, archived) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,  %s, %s, %s, DATE(%s), DATE(%s),TIME(%s),TIME(%s),%s,%s)"
		#sql  =  "(user int, tasktype int, priority int, graph_at int, id int, graph_to int, short TEXT, full TEXT, datatype int, timetype int, timestamp DATETIME, startdate DATE, stopdate DATE, time TIME, duration TIME, price int, archived int)"

		#id=uuid.uuid4().int
		id=int( uuid.uuid4().time_low ) # time_low
		#stopdate = datetime.datetime.strptime(stopdate,"%Y-%m-%d %H:%M:%S")
		timestamp = datetime.datetime.now()
		plan = text
		cursor.execute(sql, (str(user_id), tasktype, priority,graph_at,id,graph_to,plan,full,datatype,timetype,'0','0',timestamp,startdate,stopdate,time,duration,price,'0'))
		connection.commit()
		return text+" is added task to list"

	except Exception as e:
		print("mysql error addToLitst:{}".format(e))

def mysqlSetTime(user_id, graph_to, hours):
	try:

		#time  = datetime.datetime.strptime("1970-01-01 08:00:00", "%Y-%m-%d %H:%M:%S")
		hour = int(hours.partition(':')[0])
		time=datetime.timedelta(hours=hour)# + time

		mins = int(hours.partition(':')[2])
		time=time+datetime.timedelta(minutes=mins)

		cursor = connection.cursor()
		sql   = "UPDATE `adaptiveV15` SET  time=%s WHERE user =%s AND id =%s"
		cursor.execute(sql, (time, str(user_id), graph_to))
		connection.commit()

		return str(hours)+" is done"

	except Exception as e:
		print("mysql error mysqlSetTime:{}".format(e))


def mysqlDeleteAll(user_id):
	try:
		cursor = connection.cursor()
		sql   = "delete FROM `adaptiveV15` WHERE user =%s"
		cursor.execute(sql, str(user_id))
		connection.commit()

		return "all tasks are deleted from list"

	except Exception as e:
		print("mysql error delete all:{}".format(e))

def mysqlDelete(user_id,text):
	try:
		cursor = connection.cursor()
		sql   = "delete FROM `adaptiveV15` WHERE user =%s AND short =%s  ORDER BY timestamp ASC"
		cursor.execute(sql, (str(user_id), text))
		connection.commit()



		return text+" is deleted from list"

	except Exception as e:
		print("mysql error delete:{}".format(e))


def mysqlDeleteByID(user_id,graph_id):
	try:
		cursor = connection.cursor()
		sql   = "delete FROM `adaptiveV15` WHERE user =%s AND id =%s"
		cursor.execute(sql, (str(user_id), graph_id))
		connection.commit()


		return " is deleted from list"

	except Exception as e:
		print("mysql error deleteByID:{}".format(e))

def mysqlNearestDate():
	try:
		cursor = connection.cursor()
		sql = " select stopdate from `adaptiveV15` WHERE `stopdate` BETWEEN  NOW() AND (NOW()+INTERVAL 1 DAY) ORDER BY stopdate " #LIMIT 1 "#WHERE `id`=%s"
		cursor.execute(sql,)
		result = cursor.fetchall()
		return result

	except Exception as e:
		print("mysql error nearest:{}".format(e))

def mysqlReadEveryDay():
	try:
		cursor = connection.cursor()
		sql = " select stopdate from `adaptiveV15` WHERE `copy` = 1 ORDER BY stopdate " #LIMIT 1 "#WHERE `id`=%s"
		cursor.execute(sql,)
		result = cursor.fetchall()
		return result

	except Exception as e:
		print("mysql error everyday:{}".format(e))

def mysqlEverydayTasksTime(user_id, time):
	try:
		cursor = connection.cursor()
		sql = " select stopdate,time from `adaptiveV15` WHERE  user =%s  AND `copy` = 1 "
		cursor.execute(sql, (str(user_id) ))
		result = cursor.fetchall()

		time=datetime.timedelta(hours=0)
		for row in result:
			#ret+=str(row)
			#i+=1
			#ret+=str(i)+") "
			#ret+=str(row["stopdate"]) + " " + str(row["time"])

			one = datetime.datetime.strptime('1970-01-01 08:00:00',"%Y-%m-%d %H:%M:%S")
			two = (row["time"])#datetime.datetime.strptime((row["time"]),"%Y-%m-%d %H:%M:%S")
			
			time +=  two - one
			print("every", time)

		return time

	except Exception as e:
		print("mysql error mysqlEverydayTasksTime :{}".format(e))

def mysqlHowMuchTime(user_id, time):
	try:
		cursor = connection.cursor()
		sql = " select stopdate,time from `adaptiveV15` WHERE  user =%s  AND DATE(stopdate) = DATE(%s) "
		cursor.execute(sql, (str(user_id), time))
		result = cursor.fetchall()

		time=datetime.timedelta(hours=0)
		for row in result:
			#ret+=str(row)
			#i+=1
			#ret+=str(i)+") "
			#ret+=str(row["stopdate"]) + " " + str(row["time"])

			one = datetime.datetime.strptime('1970-01-01 08:00:00',"%Y-%m-%d %H:%M:%S")
			two = (row["time"])#datetime.datetime.strptime((row["time"]),"%Y-%m-%d %H:%M:%S")
			
			time =  two - one
			print("tasks", time)

		return time

	except Exception as e:
		print("mysql error howmuchtime:{}".format(e))

def mysqlPoolStopdate(user_id):
	try:
		cursor = connection.cursor()
		sql = " select `short`,`stopdate`,`time` from `adaptiveV15` WHERE  user =%s  AND DATE(stopdate) >= CURDATE(); "
		cursor.execute(sql, str(user_id) )
		result = cursor.fetchall()

		ret=''
		i=0
		for row in result:

			i+=1
			ret+=str(i)+") "
			ret+=str(row["short"]) + " " + str(row["stopdate"]) 


		return ret

	except Exception as e:
		print("mysql error howmuchtime:{}".format(e))

def mysqlPoolOnly(user_id):
	try:
		cursor = connection.cursor()
		sql = " select `short`,`stopdate`,`time` from `adaptiveV15` WHERE  user =%s  AND timetype = 1; "
		cursor.execute(sql, str(user_id) )
		result = cursor.fetchall()

		ret=''
		i=0
		for row in result:

			i+=1
			ret+=str(i)+") "
			ret+=str(row["short"]) 

			if(str(row["stopdate"]) != "1970-01-01"):
				ret+=" "+str(row["stopdate"]) 

			if(str(row["time"]) != "0:00:00"):
				ret+=" "+str(row["time"]) 

		return ret

	except Exception as e:
		print("mysql error howmuchtime:{}".format(e))

def mysqlPoolTimetype(user_id):
	try:
		cursor = connection.cursor()
		sql = " select `short`,`stopdate`,`time` from `adaptiveV15` WHERE  user =%s  AND timetype = 1; "
		cursor.execute(sql, str(user_id) )
		result = cursor.fetchall()

		ret=''
		i=0
		for row in result:

			i+=1
			ret+=str(i)+") "
			ret+=str(row["short"]) 

			if(str(row["stopdate"]) != "1970-01-01"):
				ret+=" "+str(row["stopdate"]) 

			if(str(row["time"]) != "0:00:00"):
				ret+=" "+str(row["time"]) 

		return ret

	except Exception as e:
		print("mysql error howmuchtime:{}".format(e))


def mysqlTomorrow(user_id, time):
	try:
		cursor = connection.cursor()
		sql = " select stopdate,time from `adaptiveV15` WHERE  user =%s AND DATE(time) = DATE(%s) AND DATE(stopdate) = DATE(%s) "
		cursor.execute(sql, (str(user_id), time, time))
		result = cursor.fetchall()
		time=datetime.timedelta(hours=24)
		time-=datetime.timedelta(hours=8)
		for row in result:
			#ret+=str(row)
			#i+=1
			#ret+=str(i)+") "
			#ret+=str(row["stopdate"]) + " " + str(row["time"])

			#one = (row["stopdate"]) 
			one = datetime.datetime.strptime('1970-01-01 08:00:00',"%Y-%m-%d %H:%M:%S")
			two = (row["time"])#datetime.datetime.strptime((row["time"]),"%Y-%m-%d %H:%M:%S")
			
			time -=  two - one

		return time

	except Exception as e:
		print("mysql error howmuchtime:{}".format(e))

def mysqlTasksByDate(user_id, time):
	try:
		cursor = connection.cursor()
		sql = " select short from `adaptiveV15` WHERE  user =%s AND DATE(stopdate) = DATE(%s) AND time=%s "
		cursor.execute(sql, (str(user_id), time, '1970-01-01 08:00:00'))
		result = cursor.fetchall()
		ret=""
		i = 0
		for row in result:
			#ret+=str(row)
			i+=1
			ret+=str(i)+") "
			ret+=str(row["short"]) 
			ret+="\n"
		return ret

	except Exception as e:
		print("mysql error TasksByDate:{}".format(e))


def mysqlDone(user_id,text):
	try:
		time=datetime.datetime.now()
		cursor = connection.cursor()
		sql   = "UPDATE `adaptiveV15` SET archived=1, time=%s WHERE user =%s AND short =%s "
		#UPDATE my_table SET my_column='new value' WHERE something='some value';
		cursor.execute(sql, (time, str(user_id), text))
		connection.commit()

		return text+" is done"

	except Exception as e:
		print("mysql error done:{}".format(e))
# time type
# 0)  none
# 1)  everyday 
def mysqlSetCopy(user_id,currentGraph,copy):
	try:
		time=datetime.datetime.now()
		cursor = connection.cursor()
		sql   = "UPDATE `adaptiveV15` SET copy=%s WHERE user =%s AND id =%s "
		cursor.execute(sql, ( copy, str(user_id), currentGraph))
		connection.commit()

		if(copy==0):
			return "none " 
		if(copy==1):
			return "everyday "  

	except Exception as e:
		print("mysql error SetCopy:{}".format(e))

def mysqlDeadline(user_id,text,stopdate):
	try:
		time=datetime.datetime.now()
		cursor = connection.cursor()
		sql   = "UPDATE `adaptiveV15` SET time=%s WHERE user =%s AND short =%s "
		#UPDATE my_table SET my_column='new value' WHERE something='some value';
		cursor.execute(sql, (stopdate, str(user_id), text))
		connection.commit()

		return text+" is done"

	except Exception as e:
		print("mysql error deadline:{}".format(e))


def mysqlSwap(user_id,currentGraph,swapBufferId):
	try:
		time=datetime.datetime.now()
		cursor = connection.cursor()
		sql   = "UPDATE `adaptiveV15` SET graph_at=%s WHERE user =%s AND id =%s "
		#UPDATE my_table SET my_column='new value' WHERE something='some value';
		cursor.execute(sql, (currentGraph, str(user_id),swapBufferId) )
		connection.commit()
		return "swap is done"
		
	except Exception as e:
		print("mysql error deadline:{}".format(e))




# alternative db
# https://www.digitalocean.com/community/tutorials/mongodb-ubuntu-16-04-ru
# sudo systemctl status mongodb
# sudo systemctl start mongodb
#import pymongo
#myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#mydb = myclient["mydatabase"]
#mycol = mydb["bot"]


#sql     = "(user int, tasktype int, priority int, graph_at int, id int, graph_to int, short TEXT, full TEXT,

# for this need funks planned/result
# machine or you'r data
# real or proposed or time copy
#           everyday or else        hard or not
# datatype int,    copy int,     timetype int,   t1 int, timestamp DATETIME, startdate DATE, stopdate DATE, time TIME, duration TIME, average_t TIME, 

#, price int, archived int)"


