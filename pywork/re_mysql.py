import pymysql

host = "localhost"
root = "root"
password = "123456"
database = "SRS"
db = pymysql.connect('localhost', 'root', '123456', 'SRS')
cursor = db.cursor()

'-----------------------------------------------------------------------------------'

check = """
SET foreign_key_checks = 0;
"""
cursor.execute(check)

drop_sql = """
DROP TABLE IF EXISTS tb_college;
"""
cursor.execute(drop_sql)

check = """
SET foreign_key_checks = 1;
"""
cursor.execute(check)

tb_college = """
create table tb_college
(
collid int not null auto_increment comment '学院编号',
collname varchar(50) not null comment '学院名称',
collmaster varchar(20) not null comment '院长姓名',
collweb varchar(511) default '' comment '学院网站',
primary key (collid)
);  
"""

cursor.execute(tb_college)

uni_college_collname = """
alter table tb_college add constraint uni_college_collname unique (collname);  
"""

cursor.execute(uni_college_collname)

'------------------------------------------------------------------------------'

check = """
SET foreign_key_checks = 0;
"""
cursor.execute(check)

drop_sql = """
DROP TABLE IF EXISTS tb_student;
"""
cursor.execute(drop_sql)

check = """
SET foreign_key_checks = 1;
"""
cursor.execute(check)

tb_student = """
create table tb_student
(
stuid int not null comment '学号',
sname varchar(20) not null comment '学生姓名',
gender bit default 1 comment '性别',
birth date not null comment '出生日期',
addr varchar(255) default '' comment '籍贯',
collid int not null comment '所属学院编号',
primary key (stuid)
);  
"""
cursor.execute(tb_student)

foreign_key = """
alter table tb_student add constraint fk_student_collid foreign key (collid) references tb_college (collid);  
"""

cursor.execute(foreign_key)

'-------------------------------------------------------------------------------------------'

check = """
SET foreign_key_checks = 0;
"""
cursor.execute(check)

drop_sql = """
DROP TABLE IF EXISTS tb_teacher;
"""
cursor.execute(drop_sql)

check = """
SET foreign_key_checks = 1;
"""
cursor.execute(check)

tb_teacher = """
create table tb_teacher
(
teaid int not null comment '教师工号',
tname varchar(20) not null comment '教师姓名',
title varchar(10) default '' comment '职称',
collid int not null comment '所属学院编号'
);  
"""

cursor.execute(tb_teacher)

primary_key = """
alter table tb_teacher add constraint pk_teacher primary key (teaid);  
"""

cursor.execute(primary_key)

foreign_key_primary = """
alter table tb_teacher add constraint fk_teacher_collid foreign key (collid) references tb_college (collid);  
"""

cursor.execute(foreign_key_primary)

'---------------------------------------------------------------------------------------'

check = """
SET foreign_key_checks = 0;
"""
cursor.execute(check)

drop_sql = """
DROP TABLE IF EXISTS tb_course;
"""
cursor.execute(drop_sql)

check = """
SET foreign_key_checks = 1;
"""
cursor.execute(check)

tb_course = """
create table tb_course
(
couid int not null comment '课程编号',
cname varchar(50) not null comment '课程名称',
credit tinyint not null comment '学分',
teaid int not null comment '教师工号',
primary key (couid)
);  
"""

cursor.execute(tb_course)

cours_foreogn_key = """
alter table tb_course add constraint fk_course_tid foreign key (teaid) references tb_teacher (teaid);  
"""

cursor.execute(cours_foreogn_key)

'--------------------------------------------------------------------------------'

check = """
SET foreign_key_checks = 0;
"""
cursor.execute(check)

drop_sql = """
DROP TABLE IF EXISTS tb_score;
"""
cursor.execute(drop_sql)

check = """
SET foreign_key_checks = 1;
"""
cursor.execute(check)

tb_score = """
create table tb_score
(
scid int not null auto_increment comment '选课编号',
sid int not null comment '学号',
cid int not null comment '课程编号',
seldate date comment '选课时间日期',
mark decimal(4,1) comment '考试成绩',
primary key (scid)
);  
"""

cursor.execute(tb_score)

score_foreign_key = """
alter table tb_score add constraint fk_score_sid foreign key (sid) references tb_student (stuid);  
"""

cursor.execute(score_foreign_key)

score_forengn_key_2 = """
alter table tb_score add constraint fk_score_cid foreign key (cid) references tb_course (couid);  
"""
cursor.execute(score_forengn_key_2)

'====================================================================================='

tb_college_sql = """
insert into tb_college (collname, collmaster, collweb) values 
('计算机学院', '左冷禅', 'http://www.abc.com'),
('外国语学院', '岳不群', 'http://www.xyz.com'),
('经济管理学院', '风清扬', 'http://www.foo.com');  
"""

cursor.execute(tb_college_sql)
db.commit()

sql = """
insert into tb_student (stuid, sname, gender, birth, addr, collid) values
(1001, '杨逍', 1, '1990-3-4', '四川成都', 1),
(1002, '任我行', 1, '1992-2-2', '湖南长沙', 1),
(1033, '王语嫣', 0, '1989-12-3', '四川成都', 1),
(1572, '岳不群', 1, '1993-7-19', '陕西咸阳', 1),
(1378, '纪嫣然', 0, '1995-8-12', '四川绵阳', 1),
(1954, '林平之', 1, '1994-9-20', '福建莆田', 1),
(2035, '东方不败', 1, '1988-6-30', null, 2),
(3011, '林震南', 1, '1985-12-12', '福建莆田', 3),
(3755, '项少龙', 1, '1993-1-25', null, 3),
(3923, '杨不悔', 0, '1985-4-17', '四川成都', 3);  

"""
cursor.execute(sql)
db.commit()

sql = """
insert into tb_teacher (teaid, tname, title, collid) values 
(1122, '张三丰', '教授', 1),
(1133, '宋远桥', '副教授', 1),
(1144, '杨逍', '副教授', 1),
(2255, '范遥', '副教授', 2),
(3366, '韦一笑', '讲师', 3);  
"""
cursor.execute(sql)
db.commit()


sql = """
insert into tb_course (couid, cname, credit, teaid) values 
(1111, 'Python程序设计', 3, 1122),
(2222, 'Web前端开发', 2, 1122),
(3333, '操作系统', 4, 1122),
(4444, '计算机网络', 2, 1133),
(5555, '编译原理', 4, 1144),
(6666, '算法和数据结构', 3, 1144),
(7777, '经贸法语', 3, 2255),
(8888, '成本会计', 2, 3366),
(9999, '审计学', 3, 3366);  
"""

cursor.execute(sql)
db.commit()

sql = """
insert into tb_score (sid, cid, seldate, mark) values 
(1001, 1111, '2017-09-01', 95),
(1001, 2222, '2017-09-01', 87.5),
(1001, 3333, '2017-09-01', 100),
(1001, 4444, '2018-09-03', null),
(1001, 6666, '2017-09-02', 100),
(1002, 1111, '2017-09-03', 65),
(1002, 5555, '2017-09-01', 42),
(1033, 1111, '2017-09-03', 92.5),
(1033, 4444, '2017-09-01', 78),
(1033, 5555, '2017-09-01', 82.5),
(1572, 1111, '2017-09-02', 78),
(1378, 1111, '2017-09-05', 82),
(1378, 7777, '2017-09-02', 65.5),
(2035, 7777, '2018-09-03', 88),
(2035, 9999, date(now()), null),
(3755, 1111, date(now()), null),
(3755, 8888, date(now()), null),
(3755, 9999, '2017-09-01', 92);  
"""
cursor.execute(sql)
db.commit()

db.close()
