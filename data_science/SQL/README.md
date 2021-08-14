
### PYMYSQL

1. Create database BASH:
```
mysql -u root -p
CREATE DATABASE Bot;
quit
```
2. Create backup BASH:
```
mysqldump -u root -p -f Bot > /home/popikeyshen/mydbdump.sql
```

2. Import python
```
import pymysql
```

3. Connect to database python:
```
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='*******',
                             db='Bot',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
```

4. Create table python:
```
sqlQuery  = "CREATE TABLE adaptiveV15(user int, tasktype int, priority int, ...)
```
5. Insert in to table python:
```
INSERT INTO `adaptiveV15` (`id`, `id2`, `plan`, `full_plan`, `Datetime`) VALUES (%s, %s, %s, %s, %s)"
```

6. Read
```
" SELECT `user`,`short`, `startdate`, `id` FROM `adaptiveV15` "#WHERE `id`=%s"
```
7. Delete
```
"DELETE FROM `Employee` WHERE id2 = '%s'"
```
8. Update data
```
"UPDATE `adaptiveV15` SET archived=1, time=%s WHERE user =%s AND short =%s "
```



