# coding=UTF-8

# 导入MySQL驱动:
import mysql.connector
import config
import time
time.time()
strftime = time.strftime('%Y-%m-%d', time.localtime(time.time()))
print(strftime)

select_cmd = 'select * from MESSAGE_COUNT where userNameValue = (%s)'
select_param = (18,)


add_sql = 'insert into MESSAGE_COUNT(time,groupID,groupName,userNameValue,nickName,userName,sharing,recording,attachment,map,card,note,video,text) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)'
add_param = (strftime,1,'1','1','1','1','1','1','1','1','1','1','1','text')


update_by_type_cmd = "update MESSAGE_COUNT set (%s) = (%s)  where userNameValue = (%s) and groupName = (%s) and time ="+strftime+""

update_defult_cmd = "update MESSAGE_COUNT set (%s) = 1  where userNameValue = (%s) and groupName = (%s) and time ="+strftime+""

def getconnect():
 try:
  # conn = mysql.connector.connect(**config)
  conn = mysql.connector.connect(host=config.mysql_url, user=config.mysql_userName, password=config.mysql_passWd,
                                database=config.mysql_dbName)

  conn.cursor(dictionary=True)
  return conn;
 except mysql.connector.Error as e:
  print('connect fails!{}'.format(e))



def selectOpr(sql_cmd, param):
 """
 :param sql_cmd sql 命令
 :param param 参数
 """
 conn = getconnect()
 cursor = conn.cursor(dictionary=True)
 try:
  cursor.execute(sql_cmd, param)
  fetchall = cursor.fetchall()
  return  fetchall
 except mysql.connector.Error as e:
  print('connect-- fails!{}'.format(e))
 finally:
  cursor.close()
  conn.close()


def selectByUserName(userName):
 select_by_val_cmd = 'select * from MESSAGE_COUNT where userName = (%s)'
 select_by_val_param = (userName,)
 select_opr = selectOpr(sql_cmd=select_by_val_cmd, param=select_by_val_param)
 print("selectByUserName 查询成功")
 print(select_opr)
 return select_opr

def selectGroupUserCount(userName,group,time):
 select_by_val_cmd = 'select * from MESSAGE_COUNT where userName = (%s) and groupName = (%s) and time = (%s)'
 if time == None:
  time=strftime
 select_by_val_param = (userName,group,time)
 select_opr = selectOpr(sql_cmd=select_by_val_cmd, param=select_by_val_param)
 print("selectGroupUserCount 查询成功")
 print(select_opr)
 return select_opr

def selectByGroup(groupName):
 select_by_val_cmd = 'select * from MESSAGE_COUNT where groupName = (%s)'
 select_by_val_param = (groupName,)
 select_opr = selectOpr(sql_cmd=select_by_val_cmd, param=select_by_val_param)
 return select_opr


def addDefult(groupName,userNameVal,name,nickName):
 addDefultParam = (strftime,None,groupName,userNameVal,nickName,name,'0','0','0','0','0','0','0','0')

 row = addOpra(sql_cmd=add_sql,param=addDefultParam)
 if(row == 1):
  print(row)
  print("新增初始化成功")
 else:
  print(row)
  print("新增初始化失败")


def addOpra(sql_cmd, param):
 """
 :param sql_cmd sql 命令
 :param param 参数
 """
 conn = getconnect()
 cursor = conn.cursor()
 try:
  cursor.execute(sql_cmd, param)
  conn.commit()
 except mysql.connector.Error as e:
  print('connect-- fails!{}'.format(e))
 finally:
  rowcount = cursor.rowcount
  cursor.close()
  conn.close()
  return rowcount
def update(sql_cmd, param):
 """
 :param sql_cmd sql 命令
 :param param 参数
 """
 conn = getconnect()
 cursor = conn.cursor()
 try:
  cursor.execute(sql_cmd, param)
  conn.commit()
 except mysql.connector.Error as e:
  print('connect-- fails!{}'.format(e))
 finally:
  rowcount = cursor.rowcount
  cursor.close()
  conn.close()
  return  rowcount;
def updateByType(groupName, type,userName,num):

 #update_by_type_cmd = 'update MESSAGE_COUNT set %s = %s  where userNameValue = %s and groupName = %s and time =' + strftime + ''
 update_by_type_cmd = "update MESSAGE_COUNT set (type) = %s  where userName = %s and groupName = %s and time = %s"

 #update_by_type_param = (type,num,userNameVal,groupName)

 replace = update_by_type_cmd.replace("(type)", type, 1)

 update_by_type_param = (num,userName,groupName,strftime)

 row = update(replace, update_by_type_param)

 if (row == 1):
  print(row)
  print("更新成功")
 else:
  print(row)
  print("更新失败")


#add = 'insert into MESSAGE_COUNT(time,groupID,groupName,userName,nickName,userNameValue,sharing,recording,attachment,map,card,note,video) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',['strftime',1,'1','1','1','1','1','1','1','1','1','1','1']
#add = "insert into MESSAGE_COUNT(time,groupID,groupName,userName,nickName,userNameValue,sharing,recording,attachment,map,card,note,video) values("+strftime+",1,'1','1','1','1','1','1','1','1','1','1','1')"
if __name__ == "__main__":
 # 注意把password设为你的root口令:
 # conn = mysql.connector.connect(host=config.mysql_url,user=config.mysql_userName, password=config.mysql_passWd, database=config.mysql_dbName)
 # cursor = conn.cursor()
 # 创建user表:
 #cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
 # 插入一行记录，注意MySQL的占位符是%s:

 #addOpra(sql_cmd=add_sql,param=add_param)
  addDefult("TEST",None,"TEST","TEST")
 # param = (1,)

 #updateByType("Test", 'text', "0", 7)
 #selectOpr(sql_cmd=select_cmd,param=select_param)
# select(sql_cmd=select_message_count_by_id,param=param)
 #cursor.execute(select_message_count)
 #values = cursor.fetchall()