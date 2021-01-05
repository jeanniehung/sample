import pymysql

host = "localhost"
root = "root"
password = "123456"
db = "db"
db = pymysql.connect(host=host, root=root, password=password, db=db)
cursor = db.cursor()

tb_college = '''
create table tb_college
(
collid int not null auto_increment comment '学院编号',
collname varchar(50) not null comment '学院名称',
collmaster varchar(20) not null comment '院长姓名',
collweb varchar(511) default '' comment '学院网站',
primary key (collid)
);  

'''
cursor.execute(tb_college)
db.commit()
db.close()
